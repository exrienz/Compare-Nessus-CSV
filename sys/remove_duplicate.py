import json
import sys

def remove_duplicates(json_data):
    unique_entries = []
    seen_entries = set()

    for entry in json_data:
        key = (entry["CVE"], entry["Risk"], entry["Host"], entry["Port"], entry["Name"])
        if key not in seen_entries:
            seen_entries.add(key)
            unique_entries.append(entry)

    return unique_entries

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input.json")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            data = json.load(file)

        unique_data = remove_duplicates(data)

        with open(input_file, 'w') as file:
            json.dump(unique_data, file, indent=2)

        print("Duplicates removed successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
