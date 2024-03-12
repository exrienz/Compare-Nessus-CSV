import json
import sys

def calculate_summary(data):
    summary = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0, "Total": 0}

    for entry in data:
        risk_level = entry.get("Risk", "").lower()
        if risk_level == "critical":
            summary["Critical"] += 1
        elif risk_level == "high":
            summary["High"] += 1
        elif risk_level == "medium":
            summary["Medium"] += 1
        elif risk_level == "low":
            summary["Low"] += 1

    summary["Total"] = sum(summary.values())
    return summary

def print_summary(scan_name, summary):
    print(f"Summary for {scan_name} (Critical: {summary['Critical']}, High: {summary['High']}, Medium: {summary['Medium']}, Low: {summary['Low']}, Total: {summary['Total']})")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 stat.py {json file} {scan name}")
        sys.exit(1)

    input_file = sys.argv[1]
    scan_name = sys.argv[2]

    try:
        with open(input_file, "r") as file:
            data = json.load(file)
            summary = calculate_summary(data)
            print_summary(scan_name, summary)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the provided file.")

if __name__ == "__main__":
    main()

