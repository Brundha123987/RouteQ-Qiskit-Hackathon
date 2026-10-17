
import streamlit as st
import matplotlib.pyplot as plt
from routeq import ROUTES, run_demo, state_costs

st.set_page_config(
    page_title="RouteQ Emergency Dashboard",
    page_icon="🚑",
    layout="wide",
)

st.title("🚑 RouteQ: Emergency Route Screening")
st.write("Compare illustrative emergency routes and explore Qiskit simulation results.")

st.warning(
    "Educational prototype only. These illustrative routes and risk scores "
    "must not be used for real emergency dispatch."
)

st.subheader("Route Overview")

cols = st.columns(len(ROUTES))

for col, route in zip(cols, ROUTES):
    with col:
        st.metric(route["name"], f'{route["minutes"]} min')
        st.write(f'**Risk score:** {route["risk"]}')
        st.caption(route["description"])

st.subheader("Compare Routes")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

names = [r["name"] for r in ROUTES]
risks = [r["risk"] for r in ROUTES]
times = [r["minutes"] for r in ROUTES]

axes[0].bar(names, risks)
axes[0].set_title("Risk Score — lower is better")
axes[0].set_ylabel("Risk")

axes[1].bar(names, times)
axes[1].set_title("Estimated Travel Time")
axes[1].set_ylabel("Minutes")

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.subheader("Inspect a Route")

selected_name = st.selectbox("Choose a route", names)
selected = next(r for r in ROUTES if r["name"] == selected_name)

st.write(f'**Description:** {selected["description"]}')
st.write(f'**Risk score:** {selected["risk"]}')
st.write(f'**Estimated time:** {selected["minutes"]} minutes')

st.subheader("Qiskit Simulation")

if st.button("Run route-selection simulation"):
    with st.spinner("Running simulation..."):
        try:
            circuit, counts, probabilities = run_demo(shots=1024)

            st.success("Simulation completed")
            st.write("Measurement counts")
            st.bar_chart(counts)

            costs = state_costs()
            best_index = min(range(len(costs)), key=lambda i: costs[i])
            st.write(f"Lowest-cost bitstring: `{best_index:03b}`")
            st.write(f"Objective cost: {costs[best_index]:.2f}")

            st.caption(
                "This uses a classical simulator. It does not demonstrate "
                "quantum advantage or provide real-world route guidance."
            )
        except Exception as error:
            st.error(f"Simulation failed: {error}")
