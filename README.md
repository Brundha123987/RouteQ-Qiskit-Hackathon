# RouteQ: Quantum-assisted emergency route screening

**A small Qiskit hackathon prototype** exploring how a QAOA-style circuit can encode a constrained route-selection problem.

> Important: RouteQ is an educational simulation with synthetic example values. It is not a live navigation, emergency-dispatch, or safety system. It does not claim quantum advantage or that results came from quantum hardware.

## Problem
During an emergency, responders may need to choose one route from several alternatives while balancing hazard exposure and travel time. This prototype demonstrates how a tiny binary optimization problem can be represented as a QUBO and explored with a quantum circuit.

## What makes this project distinctive
Rather than a generic coin toss or entanglement demo, RouteQ connects a Qiskit circuit to a recognizable emergency logistics scenario. The project makes the constraint explicit (select exactly one route), shows measurement outcomes, and discusses invalid solutions and limitations. We cannot claim no one has ever built a similar idea; the specific framing and experiment are our prototype.

## Model
Three qubits represent three candidate routes:
- `q0` = Route A
- `q1` = Route B
- `q2` = Route C

For bitstring `x`, the objective is:

`C(x) = sum(risk_i * x_i) + P * (sum(x_i) - 1)^2`

The penalty `P=8` discourages selecting zero or multiple routes. The cost unitary applies phases `exp(-i * gamma * C(x))`; the mixer applies `RX(2*beta)` to each qubit. Hadamard gates initialize a uniform superposition. Measurement samples candidate bitstrings.

This is a compact QAOA-style demonstration with fixed illustrative parameters, not a parameter-optimized production solver. The chosen cost uses risk score as the objective; travel time is shown as context but not yet optimized jointly.

## Repository
- `routeq.py` — runnable Python demo and Qiskit circuit.
- `RouteQ_Hackathon.ipynb` — notebook version with explanation, circuit drawing, counts, and chart.
- `requirements.txt` — dependencies.
- `evidence/` — project/circuit overview and illustrative sample-output reference.

## Setup
Python 3.10+ recommended.

### Windows (PowerShell)
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python routeq.py
```

### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m pip install -r requirements.txt
python routeq.py
```

### Run in Jupyter
```bash
jupyter notebook RouteQ_Hackathon.ipynb
```
Run all cells from top to bottom. The notebook draws the circuit and plots measurement counts.

## How to interpret the output
- The eight basis states are all 3-bit strings.
- Valid route choices are `001` (A), `010` (B), and `100` (C).
- States with zero or multiple selected routes receive a penalty.
- Counts are stochastic and can vary with shot count/parameters.
- The lowest-risk feasible route in this toy input is Route B (risk 1.0), even though it has a longer illustrative ETA.

## Evidence policy
Regenerate the circuit drawing and output chart by running the notebook in your environment. Any screenshot submitted should be captured from your actual run. The files in `evidence/` are a conceptual diagram and a reference illustration, not proof of an IBM Quantum hardware run.

## Suggested team presentation (2 minutes)
1. **Problem (20 s):** emergency routing involves trade-offs and constraints.
2. **Encoding (30 s):** one qubit per route; a penalty enforces exactly one route.
3. **Circuit (30 s):** H initialization, diagonal cost phase, RX mixer, measurement.
4. **Results (25 s):** compare sampled states and objective values; note invalid outcomes.
5. **Limitations (15 s):** synthetic data, tiny search space, fixed parameters, no quantum advantage claim.

## Improvements if time permits
- Add travel time as a weighted term with a clearly explained trade-off.
- Sweep `gamma` and `beta` and compare average objective against random sampling.
- Add noise to demonstrate robustness limits.
- Scale only after validating the tiny model and report classical baselines honestly.

## Sources and acknowledgements
- RV University, *Qiskit Quantum Computing Hackathon — Challenge Brief, IBM Qiskit Fall Fest 2026* (team-provided PDF).
- Qiskit documentation: https://quantum.cloud.ibm.com/docs/
- Qiskit quickstart: https://quantum.cloud.ibm.com/docs/en/guides/quick-start

The circuit structure and scenario are an educational project implementation. If code or tutorial material is adapted, acknowledge the exact source and describe your changes before submission.
