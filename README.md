

# RouteQ – Quantum-Assisted Emergency Route Screening

## Team Members
- [Harshitha S]
- [Brundha K Gowda]
- [Chandana B C]


## About the Project

During an emergency, choosing a suitable route can be difficult because the shortest route may not always be the best option. Factors such as route cost and risk also need to be considered.

RouteQ is a Qiskit-based project that explores how quantum computing can be used for emergency route screening. It uses a quantum circuit to demonstrate the concept and examines the measurement results along with route-related cost information.

This project is a prototype developed to understand the possible use of quantum computing in route selection. It is not intended to replace real-time navigation systems.

## Tools and Technologies
- Python
- Qiskit
- Jupyter Notebook
- Matplotlib

## Project Files

- `routeq.py` – Main Python program.
- `RouteQ_Hackathon.ipynb` – Jupyter Notebook containing the implementation and outputs.
- `requirements.txt` – List of Python dependencies.
- `routeq_circuit.png` – Quantum circuit diagram.
- `routeq_measurement_graph.png` – Measurement graph.
- `evidence/` – Contains the supporting project diagrams and evidence.

## Installation

Make sure Python is installed on your computer. Git is required only if you want to clone the project from GitHub.

### 1. Download the project

Clone the repository using:

```bash
git clone https://github.com/YOUR-USERNAME/RouteQ-Qiskit-Hackathon.git
cd RouteQ-Qiskit-Hackathon
```

Replace `YOUR-USERNAME` with your GitHub username. If you have already downloaded the project, open CMD in the project folder instead.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

For Windows CMD, activate it using:

```cmd
.venv\Scripts\activate.bat
```

### 3. Install the required packages

```bash
python -m pip install -r requirements.txt
```

## Running the Project

### Run the Python program

After activating the virtual environment, execute:

```bash
python routeq.py
```

### Run the Jupyter Notebook

Start Jupyter Notebook with:

```bash
python -m jupyter notebook
```

Open `RouteQ_Hackathon.ipynb` in the browser and run the cells using **Run → Run All Cells**. The notebook displays the implementation and its outputs.

## Understanding the Output

The project includes a quantum circuit diagram and a measurement graph to help explain the circuit and its results.

- **Quantum circuit:** Shows the quantum operations used in the implementation.
- **Measurement results:** Show the outcomes recorded when the circuit is executed.
- **Measurement graph:** Presents the measurement results visually.
- **Route-related costs:** Help illustrate the route-screening concept used in the project.

The results depend on the implementation and its inputs. They demonstrate the project concept rather than confirming the safety of a real-world emergency route.

## Future Scope

The project could be extended by adding real traffic information, more route constraints, and comparisons with classical route-selection methods. Testing with realistic route data would also help evaluate its usefulness.

## Conclusion

RouteQ gave us an opportunity to explore Qiskit and understand how quantum circuits and measurement results can be used in a route-screening prototype. It provides a starting point for further work on quantum-assisted route selection.


