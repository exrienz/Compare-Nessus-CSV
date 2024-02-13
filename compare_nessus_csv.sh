#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <old.csv> <new.csv>"
    exit 1
fi

fileA="$1"
fileB="$2"

temp_fileA="new_$fileA"
temp_fileB="new_$fileB"
output_file="report.csv"

python3 parse_csv.py "$fileA" "$temp_fileA"
python3 parse_csv.py "$fileB" "$temp_fileB"
python3 compare.py "$temp_fileA" "$temp_fileB" > new_output.csv
python3 delCol.py new_output.csv "$output_file"

# Remove temporary files
rm "$fileA" "$fileB" "$temp_fileA" "$temp_fileB" new_output.csv
