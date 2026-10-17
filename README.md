# RouteQ – Quantum-Assisted Emergency Route Screening

**RouteQ** is a Qiskit-based educational prototype that explores QAOA-style quantum circuit simulation for emergency route screening and compares the results with a classical exhaustive-search baseline.

## Live Demo

[RouteQ Emergency Dashboard · Streamlit](https://routeq-qiskit-hackathon-nk8mbyxwraewlntdhkjuch.streamlit.app/)

The interactive dashboard demonstrates route selection, simulation results, and classical comparison. The application uses a classical simulator and illustrative route data; it is not a real-time navigation system.

## Team Members

- Harshitha S
- Brundha K Gowda
- Chandana B C

## About the Project

During an emergency, choosing a suitable route can be difficult because the shortest route may not always be the best option. Factors such as travel time and risk may need to be considered.

RouteQ explores how quantum computing concepts can be applied to a small route-selection problem. It uses a QAOA-style quantum circuit to sample candidate route selections and compares the observed outcomes with a classical exhaustive-search solution.

The current objective minimizes route risk while encouraging exactly one route to be selected. Travel time is displayed as additional route information but is not included in the optimization objective.

This project demonstrates quantum circuits, statevector simulation, measurement sampling, optimization constraints, and classical comparison. It does not claim quantum advantage or guarantee real-world route safety.

## Tools and Technologies

- Python
- Qiskit
- NumPy
- Streamlit
- Jupyter Notebook
- Matplotlib

## Project Files

- `routeq.py` – Main Qiskit program and QAOA-style simulation.
- `classical_baseline.py` – Classical exhaustive search and comparison with simulation results.
- `dashboard.py` – Streamlit dashboard for exploring the project.
- `RouteQ_Hackathon.ipynb` – Jupyter Notebook containing the implementation and outputs, if included in the repository.
- `requirements.txt` – Python dependencies.
- `routeq_circuit.png` – Quantum circuit diagram, if included.
- `routeq_measurement_graph.png` – Measurement graph, if included.
- `evidence/` – Supporting diagrams and evidence, if included.

## Installation

Python and Git are required to clone and run the project locally.

### 1. Clone the Repository

Replace `YOUR-USERNAME` with the GitHub username of the repository you want to clone.

```bash
git clone https://github.com/YOUR-USERNAME/RouteQ-Qiskit-Hackathon.git
cd RouteQ-Qiskit-Hackathon
```

Alternatively, download the repository as a ZIP file from GitHub.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

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

The program builds a quantum circuit, simulates its statevector, samples measurement outcomes, and displays route costs and results.

The simulation runs on a classical computer. It does not use quantum hardware.

### Run the Classical Baseline

```bash
python classical_baseline.py
```

The classical program evaluates all eight possible bitstrings for the three-route problem, identifies the feasible selections, and finds the minimum-cost feasible route. It then runs the QAOA-style simulation and compares the sampled outcomes with the classical optimum.

### Run the Streamlit Dashboard Locally

```bash
python -m streamlit run dashboard.py
```

Streamlit displays a local URL in the terminal. Open that URL in a browser to use the dashboard.

### Run the Jupyter Notebook

```bash
python -m jupyter notebook
```

Open `RouteQ_Hackathon.ipynb` if it exists in the repository, then select **Run → Run All Cells**.

## Understanding the Objective Function

The project defines three illustrative routes:

| Route   | Risk | Travel time |
| ------- | ---: | ----------: |
| Route A |    2 |  18 minutes |
| Route B |    1 |  24 minutes |
| Route C |    3 |  15 minutes |

The current optimization objective is:

[
C(x)=\sum\_{q=0}^{2}x_qr_q+
8\left(\sum\_{q=0}^{2}x_q-1\right)^2
]

Where:

- (x_q) is either 0 or 1, indicating whether a route is selected.
- (r_q) is the risk value of route (q).
- The penalty coefficient is 8.
- The penalty discourages selecting zero routes or multiple routes.

**Important:** Travel time is displayed but is not included in the objective function. Therefore, the selected route is the minimum-risk feasible route under this toy objective, not necessarily the fastest route.

## Classical Baseline and QAOA-Style Comparison

### Classical Exhaustive Search

The classical baseline evaluates all (2^3=8) possible route-selection bitstrings. The three bitstrings with exactly one selected route are feasible.

### Results

| Metric                             | Result  |
| ---------------------------------- | ------- |
| Total states evaluated classically | 8       |
| Feasible states                    | 3       |
| Classical optimal route            | Route B |
| Optimal bitstring                  | `010`   |
| Optimal objective cost             | 1.00    |
| QAOA-style simulation shots        | 4,096   |
| Feasible measurement shots         | 1,778   |
| Feasible-shot rate                 | 43.41%  |
| Optimal route observed in samples  | Yes     |

### Interpretation

Classical exhaustive search identifies Route B as the minimum-risk feasible route, with an objective cost of 1.00. The QAOA-style simulation also samples the optimal bitstring, `010`, representing Route B.

However, only 43.41% of the simulation's measurement shots selected exactly one route. Other outcomes included invalid selections such as `111`, which selects all three routes.

The classical baseline guarantees the optimum for this small problem because it checks every possible state. The simulation illustrates the variability of sampled outcomes and the importance of checking feasibility.

These results do not demonstrate quantum advantage. The statevector simulation and sampling are performed on a classical computer.

## Understanding the Output

- **Quantum circuit:** Shows the quantum operations used in the implementation.
- **Measurement results:** Show sampled bitstrings and their frequencies.
- **Measurement graph:** Visualizes measurement outcomes, if generated by the implementation.
- **Route costs:** Represent the objective values used to compare route selections.
- **Classical baseline:** Identifies the minimum-cost feasible route through exhaustive search.
- **Comparison:** Shows whether the classical optimum appears among the simulation samples.

## Limitations

- The route data is illustrative and does not represent verified real-world traffic or road hazards.
- The problem contains only three routes and eight possible bitstrings.
- The current objective minimizes risk and does not incorporate travel time.
- The QAOA-style simulation can produce infeasible or non-optimal outcomes.
- The implementation uses classical simulation and sampling, not quantum hardware.
- The experiment does not establish quantum advantage or guarantee real-world route safety.

## Future Scope

Possible extensions include:

- Incorporating travel time into the optimization objective.
- Using real traffic and road-hazard data.
- Adding route availability and other practical constraints.
- Testing larger route-selection problems.
- Comparing quantum and classical approaches using consistent objectives and evaluation metrics.

## Conclusion

RouteQ demonstrates Qiskit-based route screening, quantum-circuit simulation, and classical exhaustive search on a small illustrative problem. The classical baseline identifies Route B as the optimal feasible route under the current risk-based objective, while the QAOA-style simulation illustrates the variability of sampled outcomes.

The project provides a starting point for exploring quantum-assisted optimization without claiming quantum advantage or real-world navigation capability.
