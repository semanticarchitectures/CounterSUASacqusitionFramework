# Executable Model Prototypes

This directory hosts the canonical model specifications, MATLAB reference
implementation, and parity tests for the Counter-SUAS executable models.

## Structure
- `specs/`: Canonical scenario specs (JSON).
- `baselines/`: Expected outputs for parity testing.
- `matlab/`: MATLAB implementation of the model stubs.
- `tests/`: Test harnesses for MATLAB parity checks.

## MATLAB Usage
Run a scenario:
```
matlab -batch "addpath('04-analysis/models/matlab'); run_scenario('04-analysis/models/specs/sample-scenario.json','/tmp/out.json')"
```

Run parity tests:
```
matlab -batch "addpath('04-analysis/models/matlab'); addpath('04-analysis/models/tests'); run_parity_tests"
```

