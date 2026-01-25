# System Model Specification: Protected Regions and C-SUAS System

## 1. Purpose
Define a generic system model for Counter-SUAS protection of one or more regions, including requirements for detection, risk mitigation, and integration of data feeds, sensors, decision support, C2, and effectors.

## 2. Concept of Operations
The system protects one or more **Protected Regions** (static or dynamic) against airborne targets. Protection is achieved by:
- Ingesting **data feeds** (sensor telemetry, external tracks, airspace constraints).
- Fusing observations into **tracks**.
- Applying **decision support** policies and risk mitigation logic.
- Executing **C2 actions** and **effector tasks**.

## 3. Core Entities
### 3.1 Protected Region
Defines the spatial area(s) under protection.
- **Geometry**: Polygon, cylinder, corridor, or moving region.
- **Constraints**: Altitude floors/ceilings, no-fire zones, geofenced exclusions.
- **Risk Profile**: Tolerance for false alarms, collateral damage, and disruption.
- **Coverage Objectives**: Required detection range, update rate, and response time.

### 3.2 Threat / Target
Represents an unmanned aircraft or actor of interest.
- **Trajectory**: Pre-determined path, stochastic path, or responsive path.
- **Dynamics**: Speed, altitude, maneuverability, and signature profile.
- **Intent**: Benign, unknown, or hostile (probabilistic).

### 3.3 Counter-SUAS System
The system-of-systems that detects, identifies, and mitigates threats.
- **Data Feeds**: External tracks, ADS-B, RF spectrum, weather, terrain, and alerts.
- **Sensors**: Radar, RF, EO/IR, acoustic, or other modalities.
- **Decision Support**: Fusion, classification, threat assessment, and ROE checks.
- **Command & Control**: Operator UI, policy enforcement, and tasking.
- **Effectors**: Non-kinetic (EW, takeover) and kinetic (interceptors).

## 4. Requirements Model (Generic)
### 4.1 Detection Requirements
- **Pd vs. Range**: Probability of detection as a function of range, sensor type, and target signature.
- **Latency**: Maximum time from detection to C2 display.
- **Coverage**: Minimum coverage of each Protected Region volume.
- **Track Continuity**: Maximum allowable track drop rate.

### 4.2 Risk Mitigation Requirements
- **False Alarm Rate (FAR)**: Maximum alerts per time window.
- **Collateral Risk**: Constraints on effector use within protected and adjacent regions.
- **ROE Compliance**: Human-in-the-loop or automated thresholds by asset profile.
- **Safety Interlocks**: No-fire and safety exclusion compliance.

### 4.3 Decision Support Requirements
- **Classification Confidence**: Minimum confidence for hostile declaration.
- **Response Time**: Max time from threat declaration to mitigation action.
- **Explainability**: Logging of decisions and rationale.

## 5. Detection Model (Generic)
Probability of detection is modeled as:
```
Pd = f(sensor_type, range, orientation, relative_velocity, clutter, weather)
```
Where:
- **sensor_type**: modality-specific response curve.
- **range**: distance to target.
- **orientation**: aspect angle and target cross-section.
- **relative_velocity**: closing rate affecting signal processing.
- **clutter/weather**: environmental impacts.

## 6. Region and Scenario Configuration
### 6.1 Region Types
- **Static Polygon**: Fixed perimeter.
- **Volume**: 3D bounded region with altitude limits.
- **Corridor**: Path protection (e.g., convoy route).
- **Moving Region**: Dynamic region tied to asset position.

### 6.2 Scenario Inputs
- **Region Set**: One or more Protected Regions.
- **Threat Set**: One or more targets with trajectories.
- **Sensor Suite**: Sensor types, placements, and performance curves.
- **Policy Set**: ROE, false alarm tolerance, mitigation permissions.

## 7. System Interfaces
### 7.1 Inputs
- Sensor telemetry, external tracks, geospatial data, policy updates.
### 7.2 Outputs
- Tracks, alerts, mitigation tasking, and audit logs.

## 8. Metrics and Outputs
- **Operational KPIs**: Pd, FAR, time-to-alert, time-to-mitigate.
- **Resource Metrics**: Effector utilization, operator workload.
- **Acquisition Metrics**: Cost, schedule, staffing impacts.

