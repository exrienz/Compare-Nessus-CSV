import csv
import sys

def extract_columns(input_file, output_file):
    columns_to_keep = ["Status", "CVE", "Risk", "Host", "Name", "Solution"]

    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.DictReader(csv_in)
        writer = csv.DictWriter(csv_out, fieldnames=columns_to_keep)

        # Write header
        writer.writeheader()

        for row in reader:
            # Extract only the specified columns
            filtered_row = {key: row[key] for key in columns_to_keep}
            writer.writerow(filtered_row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file.csv output_file.csv")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        extract_columns(input_file_path, output_file_path)
