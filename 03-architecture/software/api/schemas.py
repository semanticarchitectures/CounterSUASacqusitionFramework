from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class EntityType(str, Enum):
    THREAT = "threat"
    NON_THREAT = "non_threat"
    SENSOR = "sensor"
    EFFECTOR = "effector"
    PROTECTED_ASSET = "protected_asset"

class Position(BaseModel):
    lat: float
    lon: float
    alt: float
    timestamp: datetime

class Velocity(BaseModel):
    vx: float  # m/s
    vy: float
    vz: float

class EntityState(BaseModel):
    entity_id: str
    entity_type: EntityType
    position: Position
    velocity: Velocity
    signature: Dict[str, Any] = Field(default_factory=dict) # RCS, Thermal, etc.

class Detection(BaseModel):
    sensor_id: str
    timestamp: datetime
    detected_type: Optional[EntityType] = None
    position_estimate: Position
    confidence: float = Field(ge=0.0, le=1.0)
    raw_data: Dict[str, Any] = Field(default_factory=dict)

class Track(BaseModel):
    track_id: str
    first_detected: datetime
    last_updated: datetime
    current_state: EntityState
    history: List[Position] = Field(default_factory=list)
    classification: EntityType
    classification_confidence: float

class EngagementStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILURE = "failure"
    ABORTED = "aborted"

class EngagementTask(BaseModel):
    task_id: str
    effector_id: str
    target_track_id: str
    start_time: datetime
    status: EngagementStatus = EngagementStatus.PENDING
    parameters: Dict[str, Any] = Field(default_factory=dict)

class ProtectedArea(BaseModel):
    name: str
    geometry_type: str  # POLYGON, CORRIDOR, VOLUME, MOVING
    coordinates: List[Position]
    altitude_limits: Optional[Dict[str, float]] = None
    risk_profile: Dict[str, Any] = Field(default_factory=dict)

class ComponentConfig(BaseModel):
    component_id: str
    component_type: str
    position: Position
    orientation: Dict[str, float] = Field(default_factory=dict) # yaw, pitch, roll
    parameters: Dict[str, Any] = Field(default_factory=dict)

class TrafficProfile(BaseModel):
    profile_name: str
    entity_type: EntityType
    trajectory_type: str # SCRIPTED, STOCHASTIC, REACTIVE
    parameters: Dict[str, Any] = Field(default_factory=dict)
    arrival_rate: float # entities per hour

class ScenarioConfig(BaseModel):
    scenario_id: str
    name: str
    description: str
    protected_areas: List[ProtectedArea]
    sensors: List[ComponentConfig]
    effectors: List[ComponentConfig]
    traffic_profiles: List[TrafficProfile]
    rules_of_engagement: Dict[str, Any] = Field(default_factory=dict)
    environment_config: Dict[str, Any] = Field(default_factory=dict)

class WorldState(BaseModel):
    timestamp: datetime
    entities: List[EntityState]
    environment: Dict[str, Any] = Field(default_factory=dict) # Weather, terrain refs
