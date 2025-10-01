import streamlit as st
import json
import os

# 🌱 Data path
SUBMISSION_FILE = "data/student_submissions.json"

# 🌌 Load existing submissions
def load_submissions():
    if not os.path.exists(SUBMISSION_FILE):
        return []
    with open(SUBMISSION_FILE, "r") as f:
        return json.load(f)

# 🌸 Save new submission
def save_submission(entry):
    submissions = load_submissions()
    submissions.append(entry)
    with open(SUBMISSION_FILE, "w") as f:
        json.dump(submissions, f, indent=2)

# 🌱 Metaphor submission form
def show_metaphor_form(user_id="anonymous"):
    st.header("🌸 Suggest a Quantum Metaphor")
    st.markdown("Help us describe quantum gates with poetic clarity.")

    gate = st.selectbox("Which gate is your metaphor for?", ["Hadamard", "Pauli-X", "Pauli-Y", "Pauli-Z", "Measurement"])
    metaphor = st.text_area("Your poetic metaphor", placeholder="e.g., The coin flips into quantum twilight...")
    author = st.text_input("Your name or alias (optional)", value=user_id)

    if st.button("Submit Metaphor"):
        if metaphor.strip():
            entry = {
                "gate": gate,
                "metaphor": metaphor.strip(),
                "author": author,
                "timestamp": str(st.session_state.get("timestamp", ""))
            }
            save_submission(entry)
            st.success("🌱 Your metaphor has been planted!")
        else:
            st.warning("Please write a metaphor before submitting.")

# 🌟 Display recent submissions
def show_recent_metaphors():
    st.subheader("🌼 Recent Metaphors from the Garden")
    submissions = load_submissions()
    if not submissions:
        st.info("No metaphors yet — be the first to plant one!")
    else:
        for entry in reversed(submissions[-5:]):
            st.markdown(f"**{entry['gate']}** → *{entry['metaphor']}* — _{entry['author']}_")
