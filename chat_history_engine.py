import json
import os

history_file = "chat_history.json"


def save_chat(user, ai):

    data = []

    if os.path.exists(history_file):

        with open(history_file, "r") as f:
            data = json.load(f)

    data.append({
        "user": user,
        "ai": ai
    })

    with open(history_file, "w") as f:
        json.dump(data, f, indent=4)


def load_history():

    if not os.path.exists(history_file):
        return []

    with open(history_file, "r") as f:
        return json.load(f)