import json
import sys

def update_vpr_score(file_a_path, file_b_path, output_file_path):
    # Read data from fileA.json
    with open(file_a_path, 'r') as file_a:
        data_a = json.load(file_a)

    # Read data from fileB.json
    with open(file_b_path, 'r') as file_b:
        data_b = json.load(file_b)

    # Create a dictionary for quick lookups based on CVE
    cve_dict = {entry['CVE']: entry['VPR Score'] for entry in data_a}

    # Update VPR Score in fileB.json if CVE exists in both files
    for entry_b in data_b:
        cve = entry_b.get('CVE')
        vpr_score = cve_dict.get(cve)
        if vpr_score is not None:
            entry_b['VPR Score'] = vpr_score

    # Write the updated data to a new file
    with open(output_file_path, 'w') as output_file:
        json.dump(data_b, output_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <fileA.json> <fileB.json> <output_file.json>")
        sys.exit(1)

    file_a_path = sys.argv[1]
    file_b_path = sys.argv[2]
    output_file_path = sys.argv[3]

    update_vpr_score(file_a_path, file_b_path, output_file_path)
