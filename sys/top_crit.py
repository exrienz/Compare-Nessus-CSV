import json
import sys

def get_vpr_score(item):
    return float(item.get('VPR Score', 0))

def main(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Create a list to store unique vulnerabilities
    unique_vulnerabilities = []

    # Create a set to check for unique CVEs
    unique_cves = set()

    # Filter items with risk levels Critical to High
    filtered_data = [item for item in data if item['Risk'] in ['Critical', 'High']]

    # Iterate through filtered data and add unique vulnerabilities to the list
    for item in filtered_data:
        cve = item['CVE']
        if cve not in unique_cves:
            unique_cves.add(cve)
            unique_vulnerabilities.append(item)

    # Sort unique vulnerabilities based on VPR score (if available)
    sorted_data = sorted(unique_vulnerabilities, key=lambda x: (get_vpr_score(x), x['Host']), reverse=True)

    # Display the top 10 unique vulnerabilities
    print("Top 10 Unique Vulnerabilities (Risk: Critical to High):")
    for index, vulnerability in enumerate(sorted_data[:10]):
        print(f"{index + 1}. CVE: {vulnerability['CVE']}, Risk: {vulnerability['Risk']}, VPR Score: {get_vpr_score(vulnerability)}")
        print(f"   Name: {vulnerability['Name']}")
        print(f"   Solution: {vulnerability['Solution']}")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 stat.py {json_file}")
        sys.exit(1)

    json_file = sys.argv[1]
    main(json_file)
