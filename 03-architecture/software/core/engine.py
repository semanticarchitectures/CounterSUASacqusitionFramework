import math
import random
from datetime import datetime, timedelta
from typing import List, Dict
from api.interfaces import BaseEntity, BaseSensor, BaseEffector, C2Engine
from api.schemas import WorldState, EntityState, Position, Velocity, EntityType, Detection, Track, EngagementTask, EngagementStatus
from api.metrics import SimulationMetrics

class SimulationEngine:
    def __init__(self, start_time: datetime):
        self.world_state = WorldState(timestamp=start_time, entities=[])
        self.sensors: List[BaseSensor] = []
        self.effectors: List[BaseEffector] = []
        self.c2_engine: C2Engine = None
        self.metrics = SimulationMetrics(
            total_threats=0, detected_threats=0, neutralized_threats=0, false_alarms=0
        )
        self.active_tracks: Dict[str, Track] = {}
        self.active_tasks: List[EngagementTask] = []

    def add_entity(self, entity_state: EntityState):
        self.world_state.entities.append(entity_state)
        if entity_state.entity_type == EntityType.THREAT:
            self.metrics.total_threats += 1

    def step(self, delta_t: float):
        """Perform one simulation time step (seconds)."""
        new_timestamp = self.world_state.timestamp + timedelta(seconds=delta_t)
        
        # 1. Update Entity Physics
        for entity in self.world_state.entities:
            # Simplified constant velocity update
            entity.position.lat += (entity.velocity.vy * delta_t) / 111111.0 # Very rough approx
            entity.position.lon += (entity.velocity.vx * delta_t) / (111111.0 * math.cos(math.radians(entity.position.lat)))
            entity.position.alt += entity.velocity.vz * delta_t
            entity.position.timestamp = new_timestamp
        
        self.world_state.timestamp = new_timestamp

        # 2. Sensing
        all_detections: List[Detection] = []
        for sensor in self.sensors:
            all_detections.extend(sensor.sense(self.world_state))

        # 3. C2 / COP Update (Simplified Tracking)
        self._update_tracks(all_detections)

        # 4. C2 Decision Making
        if self.c2_engine:
            new_tasks = self.c2_engine.process_cop(list(self.active_tracks.values()), self.world_state)
            self.active_tasks.extend(new_tasks)

        # 5. Effector Execution
        for task in self.active_tasks:
            if task.status in [EngagementStatus.PENDING, EngagementStatus.IN_PROGRESS]:
                for effector in self.effectors:
                    if effector.get_status().get("id") == task.effector_id:
                        status = effector.execute_task(task, self.world_state)
                        task.status = status
                        if status == EngagementStatus.SUCCESS:
                            self._handle_neutralization(task.target_track_id)

    def _update_tracks(self, detections: List[Detection]):
        for det in detections:
            # Simple track-by-ID correlation (mock)
            track_id = f"TRK-{det.raw_data.get('true_id', 'UNK')}"
            if track_id not in self.active_tracks:
                self.active_tracks[track_id] = Track(
                    track_id=track_id,
                    first_detected=det.timestamp,
                    last_updated=det.timestamp,
                    current_state=EntityState(
                        entity_id=det.raw_data.get('true_id', 'UNKNOWN'),
                        entity_type=det.detected_type or EntityType.THREAT,
                        position=det.position_estimate,
                        velocity=Velocity(vx=0, vy=0, vz=0) # Velocity estimation omitted in MVP
                    ),
                    classification=det.detected_type or EntityType.THREAT,
                    classification_confidence=det.confidence
                )
                self.metrics.detected_threats += 1
            else:
                self.active_tracks[track_id].last_updated = det.timestamp
                self.active_tracks[track_id].current_state.position = det.position_estimate

    def _handle_neutralization(self, track_id: str):
        if track_id in self.active_tracks:
            true_id = self.active_tracks[track_id].current_state.entity_id
            self.world_state.entities = [e for e in self.world_state.entities if e.entity_id != true_id]
            del self.active_tracks[track_id]
            self.metrics.neutralized_threats += 1

    def get_kpis(self) -> SimulationMetrics:
        if self.metrics.total_threats > 0:
            self.metrics.prob_detection = self.metrics.detected_threats / self.metrics.total_threats
            self.metrics.prob_kill = self.metrics.neutralized_threats / self.metrics.total_threats
        return self.metrics
