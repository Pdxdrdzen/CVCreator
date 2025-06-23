import json
import os

def load_data(filename="data.json"):
    try:
        if not os.path.exists(filename):
            return {"users": []}
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Błąd dekodowania JSON!")
        return {"users": []}

def save_data(data, filename="data.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except IOError:
        print("Błąd zapisu do pliku!")