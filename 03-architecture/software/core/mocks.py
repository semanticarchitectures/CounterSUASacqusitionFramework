import random
import math
from typing import List
from api.interfaces import BaseSensor, BaseEffector, C2Engine
from api.schemas import WorldState, Detection, EntityType, EngagementTask, EngagementStatus, Track, Position

class MockRadar(BaseSensor):
    def __init__(self, sensor_id: str, position: Position, max_range: float):
        self.id = sensor_id
        self.pos = position
        self.max_range = max_range

    def sense(self, world_state: WorldState) -> List[Detection]:
        detections = []
        for entity in world_state.entities:
            dist = self._calc_dist(self.pos, entity.position)
            if dist <= self.max_range:
                # Stochastic detection (Pd curve)
                pd = 1.0 - (dist / self.max_range)**2
                if random.random() < pd:
                    detections.append(Detection(
                        sensor_id=self.id,
                        timestamp=world_state.timestamp,
                        detected_type=entity.entity_type,
                        position_estimate=entity.position, # Perfect estimation for mock
                        confidence=pd,
                        raw_data={"true_id": entity.entity_id}
                    ))
        return detections

    def _calc_dist(self, p1: Position, p2: Position) -> float:
        # Very rough Cartesian distance for prototype
        return math.sqrt((p1.lat-p2.lat)**2 + (p1.lon-p2.lon)**2) * 111111.0

    def get_config(self) -> dict:
        return {"id": self.id, "type": "RADAR", "range": self.max_range}

class MockEffector(BaseEffector):
    def __init__(self, effector_id: str, success_prob: float):
        self.id = effector_id
        self.prob = success_prob

    def execute_task(self, task: EngagementTask, world_state: WorldState) -> EngagementStatus:
        if random.random() < self.prob:
            return EngagementStatus.SUCCESS
        return EngagementStatus.FAILURE

    def get_status(self) -> dict:
        return {"id": self.id, "status": "READY"}

class MockC2(C2Engine):
    def process_cop(self, tracks: List[Track], world_state: WorldState) -> List[EngagementTask]:
        tasks = []
        for track in tracks:
            if track.classification == EntityType.THREAT and track.classification_confidence > 0.5:
                # Basic threshold based engagement
                # In a real system, we'd have weapon-target pairing. 
                # For this prototype, we'll try to find a takeover or jammer effector.
                effector_id = "TAKEOVER-SYS-01" # Target our scenario effector
                tasks.append(EngagementTask(
                    task_id=f"TASK-{track.track_id}",
                    effector_id=effector_id,
                    target_track_id=track.track_id,
                    start_time=world_state.timestamp
                ))
        return tasks

    def evaluate_roe(self, track: Track) -> bool:
        return track.classification == EntityType.THREAT
