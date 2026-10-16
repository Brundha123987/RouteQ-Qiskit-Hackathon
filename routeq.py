"""
RouteQ: Quantum-assisted emergency supply route screening
Qiskit simulator demo. This is a small educational prototype, not a deployment system.
"""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import DiagonalGate
from qiskit.quantum_info import Statevector

ROUTES = [
    {"name": "Route A", "risk": 2.0, "minutes": 18, "description": "Main road; moderate congestion"},
    {"name": "Route B", "risk": 1.0, "minutes": 24, "description": "Longer route; lower hazard exposure"},
    {"name": "Route C", "risk": 3.0, "minutes": 15, "description": "Fastest route; higher hazard exposure"},
]
PENALTY = 8.0

def state_costs():
    """Return costs for computational basis states |q2 q1 q0>."""
    costs = []
    for idx in range(8):
        bits = [(idx >> q) & 1 for q in range(3)]  # q0, q1, q2
        selected = sum(bits)
        risk = sum(bits[q] * ROUTES[q]["risk"] for q in range(3))
        # Penalize selecting zero routes or multiple routes: one-hot constraint.
        costs.append(risk + PENALTY * (selected - 1) ** 2)
    return np.asarray(costs, dtype=float)

def build_qaoa_circuit(gamma=0.55, beta=0.35, layers=2):
    """Build a compact QAOA-style circuit for a one-route selection QUBO."""
    costs = state_costs()
    qc = QuantumCircuit(3, 3)
    qc.h(range(3))  # uniform superposition over 8 candidate bitstrings
    for _ in range(layers):
        # Cost unitary U_C(gamma) = diag(exp(-i gamma C(x))).
        phases = np.exp(-1j * gamma * costs)
        qc.append(DiagonalGate(phases), [0, 1, 2])
        # Standard X mixer: exp(-i beta X) on each qubit.
        for q in range(3):
            qc.rx(2 * beta, q)
    qc.measure(range(3), range(3))
    return qc

def run_demo(shots=4096, gamma=0.55, beta=0.35, layers=2, seed=7):
    qc = build_qaoa_circuit(gamma, beta, layers)
    # Statevector simulation of the circuit before measurement, then reproducible sampling.
    unitary_circuit = qc.remove_final_measurements(inplace=False)
    sv = Statevector.from_instruction(unitary_circuit)
    probs = np.asarray(sv.probabilities(), dtype=float)
    rng = np.random.default_rng(seed)
    samples = rng.choice(8, size=shots, p=probs)
    counts = {}
    for idx in samples:
        key = format(int(idx), "03b")
        counts[key] = counts.get(key, 0) + 1
    costs = state_costs()
    ranked = sorted(range(8), key=lambda i: costs[i])
    print("RouteQ | Qiskit QAOA-style route-screening demo")
    print("SIMULATOR: Qiskit Statevector + seeded measurement sampling (not quantum hardware)")
    print(f"Shots={shots}, layers={layers}, gamma={gamma}, beta={beta}")
    print("\nRoute inputs (illustrative scenario):")
    for r in ROUTES:
        print(f"  {r['name']}: risk={r['risk']}, ETA={r['minutes']} min — {r['description']}")
    print("\nLowest-cost encoded candidates (lower is better):")
    for i in ranked[:5]:
        bits = format(i, "03b")
        selected = [ROUTES[q]["name"] for q in range(3) if (i >> q) & 1]
        print(f"  |{bits}> selects {selected or 'no route'}; objective={costs[i]:.2f}")
    print("\nMeasurement counts (bitstring is |q2 q1 q0>; q0=A, q1=B, q2=C):")
    for key, value in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
        print(f"  {key}: {value} ({value/shots:.1%})")
    best_valid = min(ROUTES, key=lambda r: r["risk"])
    print(f"\nLowest-risk feasible route from the stated toy objective: {best_valid['name']}")
    print("Interpretation: QAOA-style sampling explores candidate encodings; finite shots can return invalid or non-optimal states.")
    print("Limitation: this is a tiny synthetic example and does not demonstrate quantum advantage.")
    return qc, counts, probs

if __name__ == "__main__":
    circuit, counts, probabilities = run_demo()
    print("\nCircuit:")
    print(circuit.draw(output="text"))
