import csv
import json
import sys

def process_csv(input_file, output_file):
    # Lists to store the extracted columns
    cve_column = []
    vpr_score_column = []

    # Reading the CSV file and extracting columns
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Iterate through each row in the CSV file
        for row in csvreader:
            # Check if CVE and VPR Score columns are not empty
            if row[0] and row[-1]:
                # Extract the first column (CVE) and append to the cve_column list
                cve_column.append(row[0])
                
                # Extract the last column (VPR Score) and append to the vpr_score_column list
                vpr_score_column.append(row[-1])

    # Create a list of dictionaries with 'CVE' and 'VPR Score' as keys
    result_data = [{'CVE': cve, 'VPR Score': vpr_score} for cve, vpr_score in zip(cve_column, vpr_score_column)]

    # Output the result to a JSON file
    with open(output_file, 'w') as jsonfile:
        json.dump(result_data, jsonfile, indent=2)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py input_csv output_json")
        sys.exit(1)

    # Get input and output file paths from command-line arguments
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    # Process the CSV file and output the result to JSON
    process_csv(input_file_path, output_file_path)

    print(f"Result has been saved to {output_file_path}")
