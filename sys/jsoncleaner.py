import json
import sys

def remove_null_key(data):
    if isinstance(data, list):
        for entry in data:
            if isinstance(entry, dict) and "null" in entry:
                del entry["null"]
    elif isinstance(data, dict):
        if "null" in data:
            del data["null"]

def remove_duplicates(data):
    unique_entries = []
    for entry in data:
        if entry not in unique_entries:
            unique_entries.append(entry)
    return unique_entries

def remove_none_risk_entries(data):
    return [entry for entry in data if not ("Risk" in entry and entry["Risk"] == "None")]

def validate_and_fix_vpr_score(data):
    for entry in data:
        if "VPR Score" in entry:
            try:
                vpr_score = float(entry["VPR Score"])
                if 1.0 <= vpr_score <= 10.0:
                    continue
            except ValueError:
                pass  # Fall through to the default value
            entry["VPR Score"] = 7.0

def main():
    if len(sys.argv) != 2:
        print("Usage: script.py <json_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            json_data = json.load(file)
            remove_null_key(json_data)
            json_data = remove_duplicates(json_data)
            json_data = remove_none_risk_entries(json_data)
            validate_and_fix_vpr_score(json_data)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Unable to parse JSON in '{input_file}'.")
        sys.exit(1)

    with open(input_file, 'w') as file:
        json.dump(json_data, file, indent=2)

    print(f"JSON cleaned successfully in '{input_file}'.")

if __name__ == "__main__":
    main()
