import json
from collections import defaultdict

def process_json(json_data):
    host_data = defaultdict(lambda: {'Critical': 0, 'High': 0})

    for entry in json_data:
        risk = entry.get('Risk', '').lower()
        host = entry.get('Host', '')

        if risk == 'critical':
            host_data[host]['Critical'] += 1
        elif risk == 'high':
            host_data[host]['High'] += 1

    return host_data

def display_top_vulnerable_hosts(host_data):
    sorted_hosts = sorted(host_data.items(), key=lambda x: x[1]['Critical'] + x[1]['High'], reverse=True)[:10]

    for host, vulnerabilities in sorted_hosts:
        total_findings = vulnerabilities['Critical'] + vulnerabilities['High']
        print(f"{host} (Critical: {vulnerabilities['Critical']}, High: {vulnerabilities['High']}, Total: {total_findings})")

def main(json_file):
    try:
        with open(json_file, 'r') as file:
            json_data = json.load(file)
            host_data = process_json(json_data)
            display_top_vulnerable_hosts(host_data)
    except FileNotFoundError:
        print(f"Error: File {json_file} not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the provided file.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 script.py {json_file}")
    else:
        json_file = sys.argv[1]
        main(json_file)

