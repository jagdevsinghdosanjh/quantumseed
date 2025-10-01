import numpy as np
import matplotlib.pyplot as plt

# 🌱 Convert qubit state to Bloch sphere coordinates
def state_to_bloch_coords(state_vector):
    """
    Converts a qubit state vector to Bloch sphere coordinates.

    Parameters:
        state_vector (np.array): Qubit state |ψ⟩

    Returns:
        tuple: (x, y, z) coordinates on Bloch sphere
    """
    alpha, beta = state_vector
    x = 2 * np.real(np.conj(alpha) * beta)
    y = 2 * np.imag(np.conj(alpha) * beta)
    z = np.abs(alpha)**2 - np.abs(beta)**2
    return x, y, z

# 🌌 Plot Bloch sphere with current qubit state
def plot_bloch_sphere(state_vector, show_metaphor=False, gate_name=None):
    """
    Renders the Bloch sphere and plots the qubit state.

    Parameters:
        state_vector (np.array): Qubit state |ψ⟩
        show_metaphor (bool): Whether to overlay poetic metaphor
        gate_name (str): Optional gate name for metaphor context
    """
    x, y, z = state_to_bloch_coords(state_vector)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Draw sphere
    u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
    ax.plot_surface(np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v),
                    color='lightblue', alpha=0.2, linewidth=0)

    # Draw axes
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='X')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='Y')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='Z')

    # Plot qubit state
    ax.quiver(0, 0, 0, x, y, z, color='purple', linewidth=2, label='|ψ⟩')

    # Labels and view
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.view_init(elev=30, azim=45)

    # Optional poetic metaphor
    if show_metaphor and gate_name:
        metaphors = {
            "Hadamard": "🌗 The coin flips into quantum twilight.",
            "Pauli-X": "🪞 The mirror of quantum truth reflects your state.",
            "Pauli-Y": "🌊 The tide of phase flows sideways.",
            "Pauli-Z": "🌑 The shadow beneath certainty deepens.",
            "Measurement": "🎭 The curtain falls, revealing reality’s choice."
        }
        metaphor = metaphors.get(gate_name, "✨ A transformation unfolds.")
        ax.text2D(0.5, 0.95, metaphor, transform=ax.transAxes,
                  ha='center', va='top', fontsize=10, color='darkslategray')

    return fig
