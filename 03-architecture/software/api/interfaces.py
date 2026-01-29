from abc import ABC, abstractmethod
from typing import List, Optional
from api.schemas import WorldState, Detection, Track, EngagementTask, EntityState, EngagementStatus

class BaseEntity(ABC):
    @property
    @abstractmethod
    def entity_id(self) -> str:
        pass

    @abstractmethod
    def update_state(self, delta_t: float, world_context: WorldState) -> EntityState:
        """Update the physical state of the entity based on time step and environment."""
        pass

class BaseSensor(ABC):
    @abstractmethod
    def sense(self, world_state: WorldState) -> List[Detection]:
        """Perform sensing logic and return a list of detections."""
        pass

    @abstractmethod
    def get_config(self) -> dict:
        """Return sensor physical parameters (range, FOV, etc.)."""
        pass

class BaseEffector(ABC):
    @abstractmethod
    def execute_task(self, task: EngagementTask, world_state: WorldState) -> EngagementStatus:
        """Execute a mitigation task against a target."""
        pass

    @abstractmethod
    def get_status(self) -> dict:
        """Return health and availability status."""
        pass

class C2Engine(ABC):
    @abstractmethod
    def process_cop(self, tracks: List[Track], world_state: WorldState) -> List[EngagementTask]:
        """Process the Common Operating Picture and generate engagement tasks."""
        pass

    @abstractmethod
    def evaluate_roe(self, track: Track) -> bool:
        """Determine if an engagement is permitted based on current rules."""
        pass
