import json

def load(path="settings.json"):
    with open(path) as f:
        return json.load(f)

def save(data, path="settings.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
