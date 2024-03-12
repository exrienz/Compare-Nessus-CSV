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
    if len(sys.argv) != 3:
        print("Usage: Compare_env.py <prod_json_file> <nonProd_json_file>")
        sys.exit(1)

    prod_file_path = sys.argv[1]
    non_prod_file_path = sys.argv[2]

    prod_data = load_json(prod_file_path)
    non_prod_data = load_json(non_prod_file_path)

    risk_levels = ["Critical", "High", "Medium", "Low"]
    statuses = ["Open", "New", "Closed"]

    table_data = []

    for risk in risk_levels:
        for status in statuses:
            prod_count = count_vulnerabilities(prod_data, risk, status)
            non_prod_count = count_vulnerabilities(non_prod_data, risk, status)
            total_count = prod_count + non_prod_count
            table_data.append([risk, status, prod_count, non_prod_count, total_count])

    headers = ["Risk", "Status", "Prod Count", "NonProd Count", "Total"]

    print(tabulate(table_data, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()

