import json
import sys
from tabulate import tabulate  # Ensure you have the 'tabulate' library installed (install it using: pip install tabulate)

try:
    from tabulate import tabulate
except ImportError:
    print("The 'tabulate' library is not installed. Attempting to install...")
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
        from tabulate import tabulate
        print("Installation successful.")
    except Exception as e:
        print(f"Error installing 'tabulate': {e}")
        sys.exit(1)

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def count_vulnerabilities(data, risk, status):
    return sum(1 for entry in data if entry["Risk"] == risk and entry["Status"] == status)

def main():
    if len(sys.argv) != 2:
        print("Usage: Compare_env.py <json_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    data = load_json(file_path)

    risk_levels = ["Critical", "High", "Medium", "Low"]
    statuses = ["Open", "New", "Closed"]

    table_data = []

    for risk in risk_levels:
        for status in statuses:
            count = count_vulnerabilities(data, risk, status)
            table_data.append([risk, status, count])

    headers = ["Risk", "Status", "Count"]

    print(tabulate(table_data, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()

