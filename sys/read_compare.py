import json
import sys

def analyze_findings(data):
    open_new_critical = open_new_high = open_new_medium = open_new_low = 0
    closed_critical = closed_high = closed_medium = closed_low = 0
    new_critical = new_high = new_medium = new_low = 0
    aging_critical = aging_high = aging_medium = aging_low = 0
    total_open = total_closed = total_all = 0

    for entry in data:
        status = entry.get("Status", "")
        risk = entry.get("Risk", "")

        if status in ["Open", "New"]:
            if risk == "Critical":
                open_new_critical += 1
            elif risk == "High":
                open_new_high += 1
            elif risk == "Medium":
                open_new_medium += 1
            elif risk == "Low":
                open_new_low += 1

            if status == "New":
                if risk == "Critical":
                    new_critical += 1
                elif risk == "High":
                    new_high += 1
                elif risk == "Medium":
                    new_medium += 1
                elif risk == "Low":
                    new_low += 1

            if status == "Open":
                if risk == "Critical":
                    aging_critical += 1
                elif risk == "High":
                    aging_high += 1
                elif risk == "Medium":
                    aging_medium += 1
                elif risk == "Low":
                    aging_low += 1

        elif status == "Closed":
            if risk == "Critical":
                closed_critical += 1
            elif risk == "High":
                closed_high += 1
            elif risk == "Medium":
                closed_medium += 1
            elif risk == "Low":
                closed_low += 1

        total_all += 1
        if status in ["Open", "New"]:
            total_open += 1
        elif status == "Closed":
            total_closed += 1

    print("Total New & Open Critical Finding:", open_new_critical)
    print("Total New & Open High Finding:", open_new_high)
    print("Total New & Open Medium Finding:", open_new_medium)
    print("Total New & Open Low Finding:", open_new_low)
    print(" ")
    print("Total Closed Critical Finding:", closed_critical)
    print("Total Closed High Finding:", closed_high)
    print("Total Closed Medium Finding:", closed_medium)
    print("Total Closed Low Finding:", closed_low)
    print(" ")
    print("Total New Critical Finding:", new_critical)
    print("Total New High Finding:", new_high)
    print("Total New Medium Finding:", new_medium)
    print("Total New Low Finding:", new_low)
    print(" ")
    print("Total Aging Critical Finding:", aging_critical)
    print("Total Aging High Finding:", aging_high)
    print("Total Aging Medium Finding:", aging_medium)
    print("Total Aging Low Finding:", aging_low)
    print(" ")
    print("Total New and Open Finding:", total_open)
    print("Total Closed Finding:", total_closed)
    print("Total Finding:", total_all)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]

    with open(json_file, 'r') as file:
        try:
            data = json.load(file)
            analyze_findings(data)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in the provided file.")
            sys.exit(1)
