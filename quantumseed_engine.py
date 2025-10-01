import numpy as np

# 🌌 Quantum Gates (Single-Qubit)
GATES = {
    "Hadamard": np.array([[1, 1], [1, -1]]) / np.sqrt(2),
    "Pauli-X": np.array([[0, 1], [1, 0]]),
    "Pauli-Y": np.array([[0, -1j], [1j, 0]]),
    "Pauli-Z": np.array([[1, 0], [0, -1]]),
    "Identity": np.eye(2)
}

# 🌱 Apply a gate to the current qubit state
def apply_gate(state_vector, gate_name):
    """
    Applies a quantum gate to the qubit state.

    Parameters:
        state_vector (np.array): Current qubit state |ψ⟩
        gate_name (str): Name of the gate to apply

    Returns:
        np.array: Updated qubit state
    """
    gate = GATES.get(gate_name, GATES["Identity"])
    new_state = np.dot(gate, state_vector)

    # 🌸 Poetic transition (optional logging or metaphor trigger)
    poetic_transition(gate_name)

    return new_state

# 🌌 Measure the qubit
def measure_qubit(state_vector):
    """
    Simulates measurement of the qubit in the computational basis.

    Parameters:
        state_vector (np.array): Current qubit state |ψ⟩

    Returns:
        tuple: (measurement outcome, probability)
    """
    probabilities = np.abs(state_vector) ** 2
    outcome = np.random.choice([0, 1], p=probabilities)
    return outcome, probabilities[outcome]

# 🌸 Poetic Transition Handler
def poetic_transition(gate_name):
    """
    Prints or logs poetic metaphor for a gate transition.

    Parameters:
        gate_name (str): Name of the gate applied
    """
    metaphors = {
        "Hadamard": "🌗 The coin flips into quantum twilight.",
        "Pauli-X": "🪞 The mirror of quantum truth reflects your state.",
        "Pauli-Y": "🌊 The tide of phase flows sideways.",
        "Pauli-Z": "🌑 The shadow beneath certainty deepens.",
        "Identity": "🧘 The qubit rests in stillness."
    }

    metaphor = metaphors.get(gate_name, "✨ A transformation unfolds.")
    print(metaphor)  # Replace with Streamlit display if needed
