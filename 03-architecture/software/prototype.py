import json
import os
from datetime import datetime
from core.engine import SimulationEngine
from api.schemas import EntityState, Position, Velocity, EntityType, ScenarioConfig

def run_prototype():
    print("--- Counter-sUAS Architecture Prototype: JSON Scenarios ---")
    
    # 1. Load Configuration
    config_path = os.path.join(os.path.dirname(__file__), "scenarios/airport-protection-scenario.json")
    with open(config_path, 'r') as f:
        config_data = json.load(f)
    
    config = ScenarioConfig(**config_data)
    print(f"Loaded Scenario: {config.name}")
    print(f"Description: {config.description}")
    
    # 2. Initialize Engine
    start_time = config.protected_areas[0].coordinates[0].timestamp
    engine = SimulationEngine(start_time)
    engine.load_scenario(config)
    
    # 3. Inject a Threat based on Traffic Profiles
    # (In the future, a TrafficGenerator would automate this)
    threat_profile = next(p for p in config.traffic_profiles if p.entity_type == EntityType.THREAT)
    
    threat = EntityState(
        entity_id="DRONE-PROTOTYPE-01",
        entity_type=EntityType.THREAT,
        position=Position(lat=38.860, lon=-77.041, alt=120, timestamp=start_time),
        velocity=Velocity(vx=0, vy=-15, vz=0) # 15 m/s southward
    )
    engine.add_entity(threat)
    
    print(f"\nSimulation configured with:")
    print(f" - Sensors: {[s.component_id for s in config.sensors]}")
    print(f" - Effectors: {[e.component_id for e in config.effectors]}")
    print(f" - Active Threat: {threat.entity_id} at {threat.position.lat}, {threat.position.lon}")
    
    # 4. Run Simulation Loop
    print("\nExecuting simulation...")
    for i in range(100):
        engine.step(1.0)
        
        if engine.metrics.neutralized_threats > 0:
            print(f"T+{i+1}s: SUCCESS - Threat {threat.entity_id} neutralized by {engine.active_tasks[-1].effector_id}")
            break
            
        if i % 10 == 0:
            print(f"T+{i}s: Monitoring... Entities: {len(engine.world_state.entities)}, Tracks: {len(engine.active_tracks)}")

    # 5. Report KPIs
    kpis = engine.get_kpis()
    print("\n--- Simulation Results ---")
    print(f"Execution Time: {i+1} seconds")
    print(f"Total Threats: {kpis.total_threats}")
    print(f"Detected: {kpis.detected_threats} (Pd: {kpis.prob_detection:.2f})")
    print(f"Neutralized: {kpis.neutralized_threats} (Pk: {kpis.prob_kill:.2f})")

if __name__ == "__main__":
    run_prototype()
