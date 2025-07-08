# zippy/config.py
import json
from pathlib import Path

SETTINGS_FILE = Path(__file__).parent.parent / "settings.json"  # Finds settings file

def load():
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)
