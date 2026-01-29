# Effector Models Architecture

Effectors represent the mitigation capabilities of the C-sUAS system, ranging from non-kinetic denial to kinetic interception.

## 1. Classification of Effectors
- **Non-Kinetic**:
    - *EW (Jamming)*: Models RF interference with GPS or C2 links. Effective range is a function of power, antenna gain, and geometry.
    - *Cyber/Takeover*: Protocol-level exploitation (probabilistic success).
- **Kinetic**:
    - *Guns/CIWS*: Models ballistic trajectories and probability of hit (Ph).
    - *Guided Interceptors*: Small missiles or suicide drones with their own guidance loops.
- **Directed Energy**:
    - *HEL (Laser)*: Models energy dwell time on target for structural failure.
    - *HPM (Microwave)*: Electronic component disruption.

## 2. Performance Modeling
Each effector uses a **Stochastic Outcome Generator**:
```python
Outcome = f(Type, Geometry, Target_Hardness, Environment_Conditions)
```

## 3. Secondary Effects & Collateral Risk
- Models the falling debris from kinetic intercepts.
- Models RF interference to friendly systems (e.g., blocking friendly communication during jamming).
