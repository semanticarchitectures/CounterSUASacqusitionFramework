# Sensor Models Architecture

Sensor models provide the "eyes" of the simulated C-sUAS system. They are designed with a pluggable architecture to allow for varying levels of fidelity.

## 1. Common Sensor Interface
All models implement a base interface for configuration and data output:
- `get_detections(world_state)` -> `List[Detection]`
- `field_of_regard`: 3D volume where the sensor is active.
- `update_rate`: Hz.

## 2. Modality Specifics

### Radar Model
- **Functional**: Probabilistic detection based on Radar Cross Section (RCS), range, and clutter.
- **High-Fidelity**: Models beam-steering, Doppler processing, and multi-path effects.

### EO/IR Model
- **Detections**: Based on visual contrast and thermal signature.
- **Atmospheric Impact**: Incorporates Beers-Lambert law for signal attenuation.

### RF Detection (ESM)
- **Passive**: Geolocation based on AoA (Angle of Arrival) or TDOA (Time Difference of Arrival) of control links.

## 3. Sensor Fusion Engine
- **Track Level Fusion**: Combines tracks from multiple sensors into a single Common Operating Picture (COP).
- **Measurement Level Fusion**: Centralized processing of raw detections (e.g., Radar + RF cross-cueing).
