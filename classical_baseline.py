
"""
Classical baseline for RouteQ.

Compares exhaustive classical search with the QAOA-style
measurement results using the same objective function.
"""

from routeq import ROUTES, state_costs, run_demo


def is_feasible(bitstring):
    """A feasible solution selects exactly one route."""
    return bitstring.count("1") == 1


def run_classical_baseline():
    print("\n" + "=" * 55)
    print("ROUTEQ: CLASSICAL BASELINE AND QAOA COMPARISON")
    print("=" * 55)

    costs = state_costs()

    # Check all 8 possible bitstrings.
    candidates = []
    for idx in range(8):
        bitstring = format(idx, "03b")
        candidates.append({
            "bitstring": bitstring,
            "cost": float(costs[idx]),
            "feasible": is_feasible(bitstring),
        })

    feasible = [item for item in candidates if item["feasible"]]
    best = min(feasible, key=lambda item: item["cost"])

    print("\nCLASSICAL EXHAUSTIVE SEARCH")
    print("Method: Evaluate every possible route selection.")
    print(f"States evaluated: {len(candidates)}")
    print(f"Feasible states: {len(feasible)}")
    print(f"Best bitstring: |{best['bitstring']}>")
    print(f"Best objective cost: {best['cost']:.2f}")

    # Qubit mapping: q0 = Route A, q1 = Route B, q2 = Route C.
    selected_route = next(
        ROUTES[q]["name"]
        for q in range(3)
        if (int(best["bitstring"], 2) >> q) & 1
    )
    print(f"Best classical route: {selected_route}")

    print("\nFEASIBLE ROUTE COSTS")
    for item in feasible:
        idx = int(item["bitstring"], 2)
        route = next(
            ROUTES[q]["name"]
            for q in range(3)
            if (idx >> q) & 1
        )
        print(
            f"|{item['bitstring']}>: {route}, "
            f"objective cost = {item['cost']:.2f}"
        )

    # Run the existing QAOA-style simulation.
    print("\nRUNNING QAOA-STYLE SIMULATION")
    _, counts, _ = run_demo()

    # Keep only outcomes that select exactly one route.
    valid_counts = {
        bitstring: count
        for bitstring, count in counts.items()
        if is_feasible(bitstring)
    }
    valid_total = sum(valid_counts.values())
    total_shots = sum(counts.values())

    print("\nQAOA-STYLE RESULT COMPARISON")
    print(f"Total measurement shots: {total_shots}")
    print(f"Feasible measurement shots: {valid_total}")

    if total_shots:
        print(
            f"Feasible-shot rate: "
            f"{100 * valid_total / total_shots:.2f}%"
        )

    if valid_counts:
        best_sampled = min(
            valid_counts,
            key=lambda bitstring: costs[int(bitstring, 2)]
        )
        sampled_route_index = int(best_sampled, 2)
        sampled_route = next(
            ROUTES[q]["name"]
            for q in range(3)
            if (sampled_route_index >> q) & 1
        )
        print(f"Best feasible sampled bitstring: |{best_sampled}>")
        print(f"Best feasible sampled route: {sampled_route}")
        print(
            "Sampled route objective cost: "
            f"{costs[sampled_route_index]:.2f}"
        )
        print(
            "Optimal route sampled: "
            f"{best_sampled == best['bitstring']}"
        )
    else:
        print("No feasible route was observed in the measurements.")

    print("\nCONCLUSION")
    print(
        f"Classical exhaustive search identifies {selected_route} "
        f"as the minimum-risk feasible route."
    )
    print(
        "The QAOA-style results are stochastic samples. "
        "This small simulation does not demonstrate quantum advantage."
    )


if __name__ == "__main__":
    run_classical_baseline()
