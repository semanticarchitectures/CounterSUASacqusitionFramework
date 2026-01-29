# Analysis & Acquisition Tools

These tools bridge simulation results with procurement and deployment decisions, supporting the primary acquisition mission.

## 1. Monte Carlo Controller
Automates the execution of thousands of simulation runs:
- **Parameter Sweeps**: Automatically vary target speeds, sensor ranges, or background traffic density.
- **Stochastic Variation**: Use different seeds for sensor noise and effector success probabilities.

## 2. Sensitivity Analysis
Identifies which system parameters have the greatest impact on performance:
- *Example*: How does a 10% increase in Radar range impact the overall Base Defense success?

## 3. KPI & Metrics Engine
Calculates operational and acquisition metrics:
- **Operational**: Pd (Probability of Detection), Pk (Probability of Kill), Median Time-to-Engagement.
- **Cost-Efficiency**: Calculation of "Cost-per-Kill" and "Protection-Coverage-per-Dollar" by integrating cost models with simulation performance.

## 4. Trade-off Study Generator
Allows comparison of different system configurations:
- Compare **System A** (High-cost Radar + Kinetics) vs. **System B** (Low-cost Distributed Sensors + EW).
- Generates Pareto frontiers showing cost vs. performance trade-offs.

## 5. Export & Visualization
- **AAR (After-Action Review)**: Detailed playback of specific simulation runs.
- **Executive Summaries**: High-level dashboards for decision-makers.
