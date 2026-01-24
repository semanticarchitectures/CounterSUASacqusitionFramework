# Asset Protection Profile: Airport / Airfield

## 1. Environment Overview
- **Asset Type**: High-Value Fixed Site.
- **Geography**: Typically open terrain with significant RF noise (ATC radars, communications).
- **Constraints**: Collision avoidance with friendly aircraft, radio frequency deconfliction, high public visibility.

## 2. Specific Requirements
- **Early Identification**: Requirement to identify drones as they approach the airfield perimeter or approach/departure corridors.
- **Alerting & Low False Alarm Rate**:
    - **Threshold**: <1 false alert per 48 hours.
    - **Integration**: Must bridge to existing Air Traffic Control (ATC) or Airport Operations Center (AOC) terminals.
- **Self-Protection/Effectors**:
    - **Priority**: Non-kinetic mitigation (e.g., smart jamming, takeover) to avoid collateral damage or debris on runways.
    - **Rules of Engagement (ROE)**: Automated alerting with "human-in-the-loop" for effector activation within airfield boundaries.

## 3. Command and Control (C2)
- Must provide a unified operating picture (UOP) that includes both SUAS tracks and local ADSB/friendly aircraft data for deconfliction.
- Automated sensor fusion to reduce operator workload.

## 4. Site-Specific Customization
- **Geography**: Sensors must be positioned to cover "blind spots" created by hangars or terminal buildings.
- **Local Restrictions**: Frequency management must ensure no interference with ILS (Instrument Landing System) or VHF communications.
