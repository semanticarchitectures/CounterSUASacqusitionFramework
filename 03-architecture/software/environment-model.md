# Environment & Traffic Model

This component defines the spatial and physical context in which the simulation occurs.

## 1. Spatial Definition
- **Geospatial Engine**: Supports WGS84 coordinates and local NED (North-East-Down) frames.
- **Terrain**: Ingests DTED or GeoTIFF data to model line-of-sight (LOS) masking for sensors.

## 2. Protected Area Model
Users define volumes of interest using:
- **Polygons/Volumes**: 3D zones with associated risk levels.
- **Exclusion Zones**: No-fire zones or areas where sensor performance is degraded.

## 3. Traffic Generator
- **Non-Threat Traffic**: Models background "clutter" (civilian drones, birds, manned aircraft) to test identification logic and false alarm rates.
- **Threat Entities**: sUAS with configurable flight profiles (loitering, direct attack, swarming).
- **Trajectory Engine**:
    - *Scripted*: Waypoint-following.
    - *Dynamic*: Reactive flight (avoiding detection, responding to effectors).

## 4. Atmospheric Models
- **Weather**: Impact of rain, fog, and wind on sensor performance (EO/IR attenuation, Radar clutter) and flight dynamics.
