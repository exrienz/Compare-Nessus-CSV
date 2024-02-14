import csv
import json
import sys

def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)

    # Add "VPR Score" if not available
    for item in data:
        item.setdefault("VPR Score", "N/A")

    # Writing to CSV
    with open(csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.json output.csv")
        sys.exit(1)

    json_file = sys.argv[1]
    csv_file = sys.argv[2]

    convert_json_to_csv(json_file, csv_file)
    print(f"Conversion complete. CSV file saved as {csv_file}")
