import csv
import json
import sys

def csv_to_json(csv_file_path, json_file_path):
    # Read CSV file and convert it to a list of dictionaries
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    # Write the list of dictionaries to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_csv_file> <output_json_file>")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    output_json_file = sys.argv[2]

    csv_to_json(input_csv_file, output_json_file)
