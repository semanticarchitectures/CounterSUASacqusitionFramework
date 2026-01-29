import json
from datetime import datetime
from core.engine import SimulationEngine
from core.mocks import MockRadar, MockEffector, MockC2
from api.schemas import EntityState, Position, Velocity, EntityType, ScenarioConfig

def run_prototype():
    print("--- Counter-sUAS Architecture Prototype ---")
    start_time = datetime(2026, 6, 1, 12, 0, 0)
    
    # 1. Initialize Engine
    engine = SimulationEngine(start_time)
    
    # 2. Setup Components
    radar = MockRadar("PERIM-RADAR-01", Position(lat=38.855, lon=-77.041, alt=10, timestamp=start_time), 5000)
    effector = MockEffector("MOCK-EFF-01", 0.9)
    c2 = MockC2()
    
    engine.sensors.append(radar)
    engine.effectors.append(effector)
    engine.c2_engine = c2
    
    # 3. Add a Threat Entity (approaching airport)
    threat = EntityState(
        entity_id="DRONE-ALPHA",
        entity_type=EntityType.THREAT,
        position=Position(lat=38.860, lon=-77.041, alt=100, timestamp=start_time),
        velocity=Velocity(vx=0, vy=-10, vz=0) # Moving South towards airport
    )
    engine.add_entity(threat)
    
    print(f"Simulation started with {engine.metrics.total_threats} threat(s).")
    
    # 4. Run Simulation Loop (60 seconds)
    for i in range(60):
        engine.step(1.0) # 1 second steps
        
        if engine.metrics.neutralized_threats > 0:
            print(f"T+{i+1}s: Threat neutralized!")
            break
            
        if i % 10 == 0:
            tracks = len(engine.active_tracks)
            print(f"T+{i}s: World updated. Active Tracks: {tracks}")

    # 5. Report KPIs
    kpis = engine.get_kpis()
    print("\n--- Simulation Results ---")
    print(f"Total Threats: {kpis.total_threats}")
    print(f"Detected: {kpis.detected_threats} (Pd: {kpis.prob_detection:.2f})")
    print(f"Neutralized: {kpis.neutralized_threats} (Pk: {kpis.prob_kill:.2f})")

if __name__ == "__main__":
    run_prototype()
