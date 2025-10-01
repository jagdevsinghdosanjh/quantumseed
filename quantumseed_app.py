import streamlit as st
from quantumseed_engine import apply_gate, measure_qubit
from bloch_visualizer import plot_bloch_sphere
from quantumseed_manifest import GATE_METAPHORS

st.set_page_config(page_title="QuantumSeed", layout="wide")
# 🌸 Poetic Splash Screen
st.markdown("""
<div style='text-align: center; padding: 2rem; background-color: #f0f8ff; border-radius: 10px;'>
    <h1 style='color: #6a0dad;'>🌱 QuantumSeed</h1>
    <h3 style='color: #333;'>Planting the first qubit in every curious mind</h3>
    <p style='font-style: italic; color: #555;'>
        “Between certainty and possibility lies the quantum garden.<br>
        Each gate a whisper, each measurement a revelation.<br>
        Welcome, explorer — your journey begins with a single seed.”
    </p>
</div>
""", unsafe_allow_html=True)


# Sidebar: Educator Toggles
st.sidebar.title("Educator Controls 🌿")
show_bloch = st.sidebar.checkbox("Show Bloch Sphere", value=True)
enable_metaphors = st.sidebar.checkbox("Enable Poetic Metaphors", value=True)
feedback_mode = st.sidebar.selectbox("Student Feedback Mode", ["adaptive", "guided", "minimal"])

# Main Title
st.title("🌱 QuantumSeed")
st.subheader("Planting the first qubit in every curious mind")

# Qubit State Initialization
if "qubit_state" not in st.session_state:
    st.session_state.qubit_state = [1, 0]  # |0⟩ state

# Gate Selection
gate = st.selectbox("Choose a Quantum Gate", list(GATE_METAPHORS.keys()))
if st.button("Apply Gate"):
    st.session_state.qubit_state = apply_gate(st.session_state.qubit_state, gate)
    if enable_metaphors:
        st.markdown(f"**Metaphor:** *{GATE_METAPHORS[gate]['metaphor']}*")

# Bloch Sphere Visualization
if show_bloch:
    st.pyplot(plot_bloch_sphere(st.session_state.qubit_state))

# Measurement
if st.button("Measure Qubit"):
    outcome, prob = measure_qubit(st.session_state.qubit_state)
    st.success(f"Outcome: {outcome} with probability {prob:.2f}")

