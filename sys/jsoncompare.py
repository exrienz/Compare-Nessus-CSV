import json

def compare_json(old_data, new_data):
    result = []

    for old_entry in old_data:
        cve = old_entry.get("CVE")
        new_entry = next((entry for entry in new_data if entry.get("CVE") == cve), None)

        if new_entry:
            # Entry exists in both old and new files
            status = "Open"
            # Check and update with new values
            update_entry(old_entry, new_entry)
        else:
            # Entry exists in old but not in new
            status = "Closed"

        # Add Status to the dictionary
        old_entry["Status"] = status
        result.append(old_entry)

    for new_entry in new_data:
        cve = new_entry.get("CVE")
        if not any(entry.get("CVE") == cve for entry in old_data):
            # Entry exists in new but not in old
            new_entry["Status"] = "New"
            result.append(new_entry)

    return result

def update_entry(old_entry, new_entry):
    # Update with new values and handle invalid "VPR Score"
    for key, new_value in new_entry.items():
        if key not in old_entry or key == "Status":
            continue
        if key == "VPR Score" and not is_valid_float(new_value):
            new_value = "8.0"  # Assign default value
        old_entry[key] = new_value

def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def main(old_file, new_file, output_file):
    with open(old_file, 'r') as f_old, open(new_file, 'r') as f_new:
        old_data = json.load(f_old)
        new_data = json.load(f_new)

    compared_data = compare_json(old_data, new_data)

    with open(output_file, 'w') as f_output:
        json.dump(compared_data, f_output, indent=2)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python script.py old_json_file new_json_file output_json_file")
        sys.exit(1)

    old_file, new_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    main(old_file, new_file, output_file)
