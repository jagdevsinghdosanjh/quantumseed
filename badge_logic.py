import json
import os

# 🌱 Badge definitions
BADGES = {
    "Superposition Seeker": {
        "criteria": "Applied Hadamard gate 3 times",
        "icon": "🌗"
    },
    "Truth Reflector": {
        "criteria": "Used Pauli-X gate 3 times",
        "icon": "🪞"
    },
    "Phase Whisperer": {
        "criteria": "Used Pauli-Z or Pauli-Y gate 3 times",
        "icon": "🌑"
    },
    "Metaphor Gardener": {
        "criteria": "Submitted 1 poetic metaphor",
        "icon": "🌸"
    },
    "Quantum Explorer": {
        "criteria": "Measured qubit 5 times",
        "icon": "🎭"
    }
}

# 🌌 Badge record path
BADGE_FILE = "data/badge_records.json"

# 🌱 Initialize badge record
def load_badge_records():
    if not os.path.exists(BADGE_FILE):
        return {}
    with open(BADGE_FILE, "r") as f:
        return json.load(f)

# 🌸 Save badge record
def save_badge_records(records):
    with open(BADGE_FILE, "w") as f:
        json.dump(records, f, indent=2)

# 🧠 Update badge progress
def update_badge_progress(user_id, action):
    """
    Tracks user actions and awards badges based on criteria.

    Parameters:
        user_id (str): Unique identifier for student
        action (str): Action performed (e.g., 'Hadamard', 'SubmitMetaphor', 'Measure')
    """
    records = load_badge_records()
    user = records.get(user_id, {"actions": {}, "badges": []})

    # Track action count
    user["actions"][action] = user["actions"].get(action, 0) + 1

    # Check badge criteria
    if user["actions"].get("Hadamard", 0) >= 3 and "Superposition Seeker" not in user["badges"]:
        user["badges"].append("Superposition Seeker")
    if user["actions"].get("Pauli-X", 0) >= 3 and "Truth Reflector" not in user["badges"]:
        user["badges"].append("Truth Reflector")
    if (user["actions"].get("Pauli-Z", 0) + user["actions"].get("Pauli-Y", 0)) >= 3 and "Phase Whisperer" not in user["badges"]:
        user["badges"].append("Phase Whisperer")
    if user["actions"].get("SubmitMetaphor", 0) >= 1 and "Metaphor Gardener" not in user["badges"]:
        user["badges"].append("Metaphor Gardener")
    if user["actions"].get("Measure", 0) >= 5 and "Quantum Explorer" not in user["badges"]:
        user["badges"].append("Quantum Explorer")

    records[user_id] = user
    save_badge_records(records)

# 🌟 Display earned badges
def get_user_badges(user_id):
    records = load_badge_records()
    user = records.get(user_id, {})
    return [f"{BADGES[b]['icon']} {b}" for b in user.get("badges", [])]
