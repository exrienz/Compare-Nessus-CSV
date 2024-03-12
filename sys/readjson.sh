#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo " "
    echo "Read the json file"
    echo "Usage: $0 <path/json_file_name> <scan_name>"
    echo " "
    exit 1
fi

# Check if the input file exists
[ ! -f "$0" ] && { echo "Error: Input file not found."; exit 1; }

# Count findings by severity
critical_count=$(jq -c 'map(select(.Risk == "Critical")) | length' "$1")
high_count=$(jq -c 'map(select(.Risk == "High")) | length' "$1")
medium_count=$(jq -c 'map(select(.Risk == "Medium")) | length' "$1")
low_count=$(jq -c 'map(select(.Risk == "Low")) | length' "$1")
total_count=$(jq -c 'length' "$1")

# Identify top 5 hosts with the most Critical and High severity count
top_hosts=$(jq -c 'group_by(.Host) | map({ Host: .[0].Host, CriticalCount: map(select(.Risk == "Critical")) | length, HighCount: map(select(.Risk == "High")) | length }) | sort_by(.CriticalCount + .HighCount) | reverse | .[:5]' "$1")

# Display results
echo -e "\n=============================================================="
echo -e "\nScan Name: $2"
echo "Critical Findings: $critical_count"
echo "High Findings: $high_count"
echo "Medium Findings: $medium_count"
echo "Low Findings: $low_count"
echo "Total Findings: $total_count"
echo " "
echo -e "Top 5 Hosts with the most Critical and High severity count:\n"
echo "$top_hosts" | jq -c -r '.[] | "\(.Host)\nCritical: \(.CriticalCount)\nHigh: \(.HighCount)\nTotal: \(.CriticalCount + .HighCount)\n"'
echo "=============================================================="
