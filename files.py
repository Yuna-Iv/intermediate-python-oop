# File I/O
import json
import csv
import pickle
from pathlib import Path

BASE = Path(__file__).parent

# Text files
path = BASE / "sample.txt"
path.write_text("Hello
World
", encoding="utf-8")

with open(path, encoding="utf-8") as f:
    for line in f:
        print(line.strip())

#JSON
json_path = BASE / "data.json"
with open(json_path, "w") as f:
    json.dump({"name": "Alice", "scores": [95, 87, 92]}, f, indent=2)

with open(json_path) as f:
    print(json.load(f)["name"])   # Alice

# CSV
csv_path = BASE / "records.csv"
with open(csv_path, "w", newline="") as f:
    csv.writer(f).writerows([["name", "age", "score"], ["Alice", 30, 95], ["Bob", 25, 87]])

with open(csv_path) as f:
    for row in csv.DictReader(f):
        print(row)

# Pickle (binary serialization)
pkl_path = BASE / "data.pkl"
with open(pkl_path, "wb") as f:
    pickle.dump({"key": [1, 2, 3]}, f)

with open(pkl_path, "rb") as f:
    print(pickle.load(f))

#Safe JSON read
def read_json(filepath: str) -> dict:
    try:
        with open(filepath, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")
