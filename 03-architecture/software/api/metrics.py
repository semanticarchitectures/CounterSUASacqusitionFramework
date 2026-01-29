from pydantic import BaseModel, Field
from typing import Dict, List, Optional

class SimulationMetrics(BaseModel):
    total_threats: int
    detected_threats: int
    neutralized_threats: int
    false_alarms: int
    
    # Probabilities
    prob_detection: float = Field(default=0.0, description="Pd: Probability of Detection")
    prob_kill: float = Field(default=0.0, description="Pk: Probability of Neutralization")
    
    # Latencies (seconds)
    mean_time_to_detect: float = 0.0
    mean_time_to_neutralize: float = 0.0
    max_engagement_latency: float = 0.0

class CostMetrics(BaseModel):
    unit_procurement_cost: float
    operating_cost_per_hour: float
    cost_per_engagement: float
    total_shots_fired: int
    total_engagement_cost: float = 0.0

class AcquisitionKPIs(BaseModel):
    system_id: str
    performance: SimulationMetrics
    cost: CostMetrics
    
    cost_per_threat_neutralized: float = 0.0
    protection_efficiency_score: float = Field(ge=0.0, le=100.0) # Weighted score
