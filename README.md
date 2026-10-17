# RouteQ – Quantum-Assisted Emergency Route Screening

## Team Members

- Harshitha S
- Brundha K Gowda
- Chandana B C

## About the Project

 chandana/streamlit-dashboard
During an emergency, choosing a suitable route can be difficult because the shortest route may not always be the safest or most suitable option. Factors such as route risk, travel time, and other constraints can influence route selection.

**RouteQ** is a Qiskit-based educational prototype that explores how quantum computing concepts can be applied to emergency route screening. It uses a QAOA-style quantum circuit to explore candidate route selections and compares the simulated results with a classical exhaustive-search baseline.

The project also includes a **Streamlit dashboard** that presents route information, simulation settings, measurement results, objective costs, and the classical comparison in a visual interface.

RouteQ is a hackathon prototype designed to demonstrate quantum computing concepts. It is not a real-time navigation or emergency dispatch system.

## Project Objectives

- Explore the application of Qiskit to a simplified route-selection problem.
- Represent route selection using binary decision variables.
- Apply an objective function with a penalty for invalid route selections.
- Simulate quantum-circuit measurement outcomes using a Qiskit statevector simulator.
- Compare quantum-simulation samples with a classical exhaustive-search solution.
- Visualize route information and results through an interactive dashboard.

## Tools and Technologies

During an emergency, choosing a suitable route can be difficult because the shortest route may not always be the best option. Factors such as travel time and risk also need to be considered.

RouteQ is a Qiskit-based educational prototype that explores how quantum computing can be used for emergency route screening. It uses a QAOA-style quantum circuit to explore candidate route selections and examines the resulting measurement outcomes. A classical exhaustive-search baseline is also implemented to identify the optimal route under the same objective function.

This project demonstrates the concepts of quantum circuits, simulation, measurement, and classical comparison. It is not intended to replace real-time navigation systems or guarantee the safety of an emergency route.

Live Demo

RouteQ Emergency Dashboard · Streamlit

The interactive dashboard demonstrates route selection, simulation results, and classical comparison. The application uses a classical simulator and illustrative route data; it is not a real-time navigation system.


## Tools and Technologies

- Python
- Qiskit
- NumPy
- Jupyter Notebook
- Matplotlib
  main

- **Python** – Core programming language.
- **Qiskit** – Quantum circuit construction and simulation.
- **NumPy** – Numerical calculations and sampling.
- **Pandas** – Organizing route and measurement data.
- **Matplotlib** – Measurement-result visualization.
- **Streamlit** – Interactive dashboard.
- **Jupyter Notebook** – Interactive experimentation and demonstration.
- **Git and GitHub** – Version control and collaboration.

## Project Structure

The project includes the following files and resources:

-
## Project Files

chandana/streamlit-dashboard
- `routeq.py` – Main Python program for the RouteQ simulation.
- `dashboard.py` – Dashboard interface for displaying route information and simulation results.
- `RouteQ_Hackathon.ipynb` – Jupyter Notebook containing the implementation and outputs, if included.
- `requirements.txt` – Python dependencies.
- `routeq_circuit.png` – Quantum circuit diagram, if included.
- `routeq_measurement_graph.png` – Measurement graph, if included.
- `evidence/` – Supporting project diagrams and evidence, if included.


## How the Route Selection Model Works

RouteQ uses three illustrative candidate routes:

| Route | Risk score | Estimated travel time | Description |
|---|---:|---:|---|
| Route A | 2.0 | 18 minutes | Main road; moderate congestion |
| Route B | 1.0 | 24 minutes | Longer route; lower hazard exposure |
| Route C | 3.0 | 15 minutes | Fastest route; higher hazard exposure |

These values are synthetic inputs for demonstrating the project concept. They are not live traffic measurements or verified safety assessments.

### Binary Encoding

Each route is represented by a binary decision variable:

- `q0` represents Route A.
- `q1` represents Route B.
- `q2` represents Route C.

A value of `1` means the corresponding route is selected, while `0` means it is not selected.

The model has three binary variables, giving \(2^3 = 8\) possible bitstrings. A valid selection must choose exactly one route.

### Objective Function

The current implementation uses the following objective:

\[
C(x)=\sum_{q=0}^{2}x_qr_q+
8\left(\sum_{q=0}^{2}x_q-1\right)^2
\]

Where:

- \(x_q\) is the binary decision variable for a route.
- \(r_q\) is the risk score assigned to that route.
- The penalty coefficient is `8`.
- Lower objective costs are preferred.

The penalty discourages selecting no routes or selecting multiple routes.

**Important:** The current objective minimizes risk and enforces the one-route constraint. Travel time is displayed for context but is not included in the optimization formula.

## Quantum Simulation

The main program constructs a Qiskit circuit that:

1. Applies Hadamard gates to create a uniform superposition over the candidate bitstrings.
2. Applies a diagonal cost-phase operation based on the objective values.
3. Applies an X-rotation mixer to the qubits.
4. Repeats the cost and mixer operations for the selected number of layers.
5. Simulates the resulting state using Qiskit's statevector functionality.
6. Samples the state probabilities to generate measurement counts.

The implementation is a compact **QAOA-style educational demonstration**. It uses a custom diagonal cost operation and an X mixer, with manually specified circuit parameters.

The simulation runs on a classical computer. It does not execute on quantum hardware.

## Classical Baseline and Comparison

The classical baseline enumerates all eight possible bitstrings and evaluates their objective costs. It filters the valid one-route selections and identifies the lowest-cost feasible solution.

For the illustrative route data, the classical baseline finds:

- **Best route:** Route B
- **Best bitstring:** `010`
- **Objective cost:** `1.00`
- **Feasible states:** `3` out of `8`

The Qiskit simulation samples candidate bitstrings according to the simulated circuit's probability distribution. Some sampled bitstrings can represent invalid selections, such as choosing zero routes or multiple routes.

In one example run using 4,096 shots, gamma `0.55`, beta `0.35`, two circuit layers, and random seed `7`, the results were:

| Measurement bitstring | Count | Interpretation |
|---|---:|---|
| `111` | 1,403 | All three routes selected; invalid |
| `100` | 929 | Route C selected; valid |
| `010` | 459 | Route B selected; valid |
| `000` | 451 | No route selected; invalid |
| `001` | 390 | Route A selected; valid |
| `101` | 375 | Routes A and C selected; invalid |
| `011` | 56 | Routes A and B selected; invalid |
| `110` | 33 | Routes B and C selected; invalid |

In this example, 1,778 of the 4,096 shots were feasible, giving a feasible-shot rate of approximately **43.4%**. Route B was the best feasible route observed.

These values are an example output for the stated settings. Results may change when circuit parameters, the number of shots, or the random seed change.

This comparison demonstrates how a classical baseline can be used to evaluate a quantum-style simulation. It does **not** establish quantum advantage.

## RouteQ Dashboard

The Streamlit dashboard provides a visual interface for exploring the route-screening model and its results.

### Dashboard Features

- **Route Information:** Displays the three candidate routes, risk scores, estimated travel times, and descriptions.
- **Simulation Settings:** Allows the user to adjust measurement shots, gamma, beta, circuit layers, and random seed.
- **Classical Exhaustive Search:** Displays feasible route selections and their objective costs.
- **Qiskit Simulation Results:** Shows the sampled bitstrings, measurement counts, and objective costs.
- **Measurement Distribution:** Visualizes the measurement counts using a bar chart.
- **Feasibility Statistics:** Displays the number of feasible states and the percentage of feasible measurement shots.
- **Objective Function:** Explains the risk objective and the one-route selection penalty.
- **Encoded States:** Allows the user to inspect all eight possible bitstrings.
- **Circuit View:** Displays the generated circuit in text form.
- **Limitations Notice:** Explains that the prototype does not provide live navigation or verified emergency-routing recommendations.

### Running the Dashboard

The dashboard requires `app.py` to be in the same project directory as `routeq.py`.

After installing the project dependencies, run:

```bash
streamlit run app.py
```

Streamlit will display a local URL, usually `http://localhost:8501`. Open that URL in your browser to interact with the dashboard.

If Streamlit is not included in `requirements.txt`, install it using:

```bash
python -m pip install streamlit
```

## Installation

### Prerequisites

- Python installed on your computer.
- Git, if cloning the repository.
- VS Code or another Python editor, if desired.

### 1. Clone the Repository

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
 main

```bash
git clone https://github.com/Brundha123987/RouteQ-Qiskit-Hackathon.git
cd RouteQ-Qiskit-Hackathon
```

 chandana/streamlit-dashboard
Alternatively, download the repository as a ZIP file and extract it.

Replace `YOUR-USERNAME` with the repository owner's GitHub username. If you have already cloned the project, open a terminal in the project folder instead.
 main

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

 chandana/streamlit-dashboard
For Windows Command Prompt, activate it using:

For Windows PowerShell, activate it using:

```powershell
.\.venv\Scripts\Activate.ps1
```

For Windows Command Prompt, use:
 main

```cmd
.venv\Scripts\activate.bat
```

 chandana/streamlit-dashboard
For Windows PowerShell, use:

```powershell
.\.venv\Scripts\Activate.ps1
```

 main
### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If the dashboard dependencies are not listed in the existing requirements file, install the additional packages:

 chandana/streamlit-dashboard
```bash
python -m pip install streamlit pandas matplotlib numpy qiskit
```

## Running the Project

### Run the Main Python Program

### Run the Qiskit Simulation
 main

```bash
python routeq.py
```

 chandana/streamlit-dashboard
This runs the route-screening simulation and prints the route information, objective costs, measurement counts, and circuit representation.

The program builds the quantum circuit, simulates its statevector, samples measurement outcomes, and displays route costs and results.

The simulation uses Qiskit's statevector simulator and seeded measurement sampling. It does not run on quantum hardware.
 main

### Run the Classical Baseline

```bash
python classical_baseline.py
```

 chandana/streamlit-dashboard
This evaluates the candidate bitstrings using classical exhaustive search and compares the baseline with the Qiskit simulation.

### Run the Dashboard

```bash
streamlit run app.py
```

Open the local URL provided by Streamlit to view the dashboard.

The classical program evaluates all eight possible bitstrings for the three-route problem, identifies feasible selections, and finds the minimum-cost feasible route. It then runs the QAOA-style simulation and compares the observed outcomes with the classical optimum.
main

### Run the Jupyter Notebook

Start Jupyter Notebook:

```bash
python -m jupyter notebook
```

chandana/streamlit-dashboard
Open `RouteQ_Hackathon.ipynb` if the notebook is included in the repository, then select **Run → Run All Cells** to execute its cells.

## Understanding the Results

- **Objective cost:** Indicates the cost assigned to a candidate bitstring. Lower costs are preferred under the current model.
- **Feasible selection:** A bitstring that selects exactly one route.
- **Measurement count:** The number of times a bitstring appears in the sampled simulation outcomes.
- **Feasible-shot rate:** The proportion of sampled outcomes that select exactly one route.
- **Classical optimum:** The lowest-cost feasible solution found by checking all candidate bitstrings.
- **Quantum-style simulation:** Samples candidate bitstrings using probabilities produced by the configured circuit.

The classical baseline provides an exact solution for this small problem because it evaluates every possible bitstring. The quantum-style circuit produces a probability distribution, and its sampled results may include invalid or non-optimal candidates.

## Limitations

- Route inputs are illustrative and do not represent verified real-world conditions.
- The model uses only risk scores in its objective; travel time is not optimized.
- The simulation uses a classical statevector simulator, not quantum hardware.
- The circuit parameters are manually specified rather than optimized through a full QAOA parameter-search procedure.
- The problem contains only three candidate routes and eight possible bitstrings.
- The project does not use live traffic, GPS, maps, road closures, weather, or real-time hazard data.
- The results do not guarantee route safety and do not demonstrate quantum advantage.

**RouteQ is an educational prototype and must not be used to make real emergency-routing or dispatch decisions.**

## Future Scope

Possible future improvements include:

- Incorporating additional route constraints and a more complete route-cost model.
- Including travel time as an explicit optimization objective.
- Testing on larger synthetic route-selection problems.
- Exploring parameter optimization for the QAOA-style circuit.
- Comparing the simulation with additional classical optimization approaches.
- Adding live-data integrations and map visualizations for research and demonstration, with appropriate validation.
- Improving dashboard plots and adding more detailed performance comparisons.
- Evaluating solution quality and computational costs across different problem sizes.

Any use with real emergency data would require extensive validation, reliable data sources, and appropriate safety procedures.

## Conclusion

RouteQ explores how Qiskit, quantum-circuit simulation, and classical exhaustive search can be used to demonstrate a simplified emergency route-screening problem. The project combines a binary route-selection model, an objective function with a feasibility penalty, simulated measurement outcomes, a classical baseline, and a Streamlit dashboard.

The prototype provides a foundation for learning about quantum optimization concepts and comparing their simulated behavior with a classical solution. Further work is needed before applying such methods to realistic routing problems.

---

**Project:** RouteQ – Quantum-Assisted Emergency Route Screening  
**Developed by:** Harshitha S, Brundha K Gowda, and Chandana B C  
**Purpose:** Educational and hackathon demonstration

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
 main
