# RouteQ – Quantum-Assisted Emergency Route Screening

## Team Members

- Harshitha S
- Brundha K Gowda
- Chandana B C

## About the Project

During an emergency, choosing a suitable route can be difficult because the shortest route may not always be the best option. Factors such as travel time and risk also need to be considered.

RouteQ is a Qiskit-based educational prototype that explores how quantum computing can be used for emergency route screening. It uses a QAOA-style quantum circuit to explore candidate route selections and examines the resulting measurement outcomes. A classical exhaustive-search baseline is also implemented to identify the optimal route under the same objective function.

This project demonstrates the concepts of quantum circuits, simulation, measurement, and classical comparison. It is not intended to replace real-time navigation systems or guarantee the safety of an emergency route.

## Tools and Technologies

- Python
- Qiskit
- NumPy
- Jupyter Notebook
- Matplotlib

## Project Files

- `routeq.py` – Main Qiskit program and QAOA-style simulation.
- `classical_baseline.py` – Classical exhaustive search and comparison with simulation results.
- `RouteQ_Hackathon.ipynb` – Jupyter Notebook containing the implementation and outputs.
- `requirements.txt` – List of Python dependencies.
- `routeq_circuit.png` – Quantum circuit diagram.
- `routeq_measurement_graph.png` – Measurement graph.
- `evidence/` – Supporting project diagrams and evidence.

*Note: Verify that the listed notebook, images, and evidence files exist in the repository before submitting.*

## Installation

Make sure Python and Git are installed. Git is required if you want to clone the project from GitHub.

### 1. Download the Project

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/RouteQ-Qiskit-Hackathon.git
cd RouteQ-Qiskit-Hackathon
```

Replace `YOUR-USERNAME` with the repository owner's GitHub username. If you have already cloned the project, open a terminal in the project folder instead.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

For Windows PowerShell, activate it using:

```powershell
.\.venv\Scripts\Activate.ps1
```

For Windows Command Prompt, use:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Running the Project

### Run the Qiskit Simulation

```bash
python routeq.py
```

The program builds the quantum circuit, simulates its statevector, samples measurement outcomes, and displays route costs and results.

The simulation uses Qiskit's statevector simulator and seeded measurement sampling. It does not run on quantum hardware.

### Run the Classical Baseline

```bash
python classical_baseline.py
```

The classical program evaluates all eight possible bitstrings for the three-route problem, identifies feasible selections, and finds the minimum-cost feasible route. It then runs the QAOA-style simulation and compares the observed outcomes with the classical optimum.

### Run the Jupyter Notebook

Start Jupyter Notebook:

```bash
python -m jupyter notebook
```

Open `RouteQ_Hackathon.ipynb` in the browser and execute the cells using **Run → Run All Cells**.

## Understanding the Objective Function

The project defines three illustrative routes:

| Route | Risk | Travel time |
|---|---:|---:|
| Route A | 2 | 18 minutes |
| Route B | 1 | 24 minutes |
| Route C | 3 | 15 minutes |

The current optimization objective minimizes route risk while encouraging exactly one route to be selected.

\[
C(x)=\sum_{q=0}^{2}x_qr_q+
8\left(\sum_{q=0}^{2}x_q-1\right)^2
\]

Where:

- \(x_q\) is 0 or 1, indicating whether a route is selected.
- \(r_q\) is the risk value of route \(q\).
- The penalty coefficient is 8.
- The penalty discourages selecting zero routes or multiple routes.

**Important:** Travel time is displayed as route information but is not included in the current objective function. Therefore, the best route under this objective is not necessarily the fastest route.

## Classical Baseline and QAOA Comparison

### Classical Exhaustive Search

The classical baseline checks all \(2^3=8\) possible route-selection bitstrings. It considers the three selections containing exactly one selected route to be feasible.

### Results

| Metric | Result |
|---|---|
| Total states evaluated classically | 8 |
| Feasible states | 3 |
| Classical optimal route | Route B |
| Optimal bitstring | `010` |
| Optimal objective cost | 1.00 |
| QAOA-style simulation shots | 4,096 |
| Feasible measurement shots | 1,778 |
| Feasible-shot rate | 43.41% |
| Optimal route observed in samples | Yes |

### Interpretation

Classical exhaustive search identifies Route B as the minimum-risk feasible route, with an objective cost of 1.00. The QAOA-style simulation also samples the optimal bitstring, `010`, representing Route B.

However, only 43.41% of the simulation's measurement shots selected exactly one route. Other outcomes included invalid selections, such as `111`, which selects all three routes.

The classical baseline guarantees the optimal solution for this small problem because it checks every possible state. The simulation results illustrate how measurement outcomes can vary and why feasibility constraints must be considered when interpreting them.

## Understanding the Output

- **Quantum circuit:** Shows the quantum operations used in the implementation.
- **Measurement results:** Show the sampled bitstrings and their frequencies.
- **Measurement graph:** Provides a visual representation of the measurement outcomes.
- **Route-related costs:** Represent the objective values used to compare route selections.
- **Classical baseline:** Identifies the minimum-cost feasible route by exhaustive search.
- **Comparison:** Shows whether the optimal classical route appears among the QAOA-style simulation outcomes.

## Limitations

- The route data is illustrative and does not represent verified real-world traffic or road hazards.
- The problem includes only three routes and eight possible bitstrings.
- The current objective minimizes risk and does not incorporate travel time.
- The QAOA-style simulation can produce infeasible or non-optimal outcomes.
- The program uses classical simulation and sampling, not quantum hardware.
- This experiment does not demonstrate quantum advantage or establish real-world route safety.

## Future Scope

The project could be extended by incorporating real traffic information, travel time, route availability, and additional constraints into the objective function. Further work could compare quantum and classical approaches on larger problems using consistent objectives and evaluation metrics.

## Conclusion

RouteQ provides an educational demonstration of Qiskit-based route screening, quantum-circuit simulation, and classical exhaustive search. The classical baseline identifies Route B as the optimal feasible solution under the current risk-based objective, while the QAOA-style simulation demonstrates the variability of sampled outcomes. This provides a starting point for further investigation into quantum-assisted optimization without claiming a quantum advantage.
