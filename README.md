In the garden of possibility, one seed spins.
Not left. Not right. Not yes. Not no.
But all — until you ask.

Welcome to QuantumSeed:
Where gates sculpt wonder,
And every learner becomes a quantum gardener.

# 🌱 QuantumSeed

**Planting the first qubit in every curious mind.**  
A poetic, modular Streamlit app designed to introduce quantum computing through metaphor, visualization, and educator-facing clarity.

---

## 🌌 Vision

QuantumSeed is a single-qubit simulator that blends quantum logic with poetic metaphor. It empowers educators and students to explore superposition, gate operations, and measurement — not just through math, but through metaphor and wonder.

---

## 🧠 Features

- **Streamlit-powered UI** with educator toggles and poetic overlays
- **Bloch sphere visualization** to show qubit evolution
- **Gate metaphors** that spark curiosity and deepen intuition
- **Student badge system** for engagement and recognition
- **Metaphor submission form** to invite learner creativity

---

## 🗂️ Project Structure

quantumseed/ ├── quantumseed_app.py # Streamlit entry point ├── quantumseed_engine.py # Qubit logic and gate operations ├── bloch_visualizer.py # Bloch sphere rendering ├── quantumseed_manifest.py # Gate metaphors and educator toggles ├── badge_logic.py # Student badge and recognition system ├── suggest_metaphor.py # Student form for metaphor submissions ├── assets/ # Logo or splash visuals │ └── logo.png │ └── backgrounds/ ├── data/ # Saved metaphor suggestions │ └── student_submissions.json │ └── badge_records.json ├── styles/ # Optional custom styling │ └── poetic_theme.css ├── README.md # Project overview and educator guide └── requirements.txt # Python dependencies

Code

---
## 🧭 Educator Onboarding Guide

Welcome to *QuantumSeed*, where quantum logic meets poetic metaphor. This guide helps educators navigate the app and spark curiosity in every learner.

### 🌱 Getting Started

- Launch the app at [https://quantumseed.streamlit.app](https://quantumseed.streamlit.app)
- Use the sidebar to toggle features:
  - **Bloch Sphere**: Visualize qubit evolution
  - **Metaphors**: Enable poetic overlays for each gate
  - **Feedback Mode**: Choose adaptive, guided, or minimal feedback
  - **Badge Display**: Show student progress and recognition
  - **Metaphor Submission**: Allow students to contribute poetic insights

### 🎓 Suggested Classroom Flow

1. **Introduce Qubits**: Use Hadamard and Pauli gates to explore superposition and flips
2. **Visualize States**: Enable Bloch sphere to show quantum evolution
3. **Discuss Metaphors**: Invite students to interpret poetic overlays
4. **Measure & Reflect**: Simulate measurement and discuss probabilistic outcomes
5. **Submit Metaphors**: Encourage creative contributions
6. **Celebrate Badges**: Recognize student engagement with poetic titles

### 🧠 Tips for Engagement

- Pair gate operations with real-world analogies
- Use metaphors to bridge intuition and math
- Invite students to “plant” their own metaphors
- Host a “Quantum Garden” showcase of student submissions

### 🛠️ Troubleshooting

- If the Bloch sphere doesn’t render, check `matplotlib` installation
- For badge tracking, ensure `data/badge_records.json` is writable
- Metaphor submissions are stored in `data/student_submissions.json`

---

Would you like to scaffold a classroom activity sheet next, or design a poetic certificate generator for student recognition? The garden is ready for harvest 🌸

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/jagdevsinghdosanjh/quantumseed.git
   cd quantumseed
Install dependencies

bash
pip install -r requirements.txt
Run the app

bash
streamlit run quantumseed_app.py
🌱 Educator Mode
Use the sidebar to:

Toggle Bloch sphere visibility

Enable poetic metaphors

Choose feedback mode: adaptive, guided, or minimal

✨ Contribute a Metaphor
Students and educators can submit poetic metaphors for quantum gates via the built-in form. All submissions are stored in data/student_submissions.json.

🏆 Badges & Recognition
QuantumSeed tracks student interactions and awards poetic badges based on gate mastery and metaphor engagement. Badge logic lives in badge_logic.py.

📬 Feedback & Collaboration
We welcome poetic minds, quantum educators, and curious contributors. Open an issue, submit a pull request, or plant a metaphor.

Created with clarity and wonder by Jagdev Singh Dosanjh. Quantum curiosity begins with a single seed.