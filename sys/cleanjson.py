import json
import sys

def clean_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        # Remove "null" key and its value
        for entry in data:
            if "null" in entry:
                del entry["null"]

        # Remove exact duplicate entries
        cleaned_data = [dict(t) for t in {tuple(d.items()) for d in data}]

        # Remove entries with "Risk": "None"
        cleaned_data = [entry for entry in cleaned_data if entry.get("Risk") != "None"]

        # Write back to the same file
        with open(filename, 'w') as file:
            json.dump(cleaned_data, file, indent=4)

        print(f"File '{filename}' successfully cleaned.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        clean_json(filename)
