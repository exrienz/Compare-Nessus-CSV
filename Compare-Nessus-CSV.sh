#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <old.csv> <new.csv> <output_file_name.csv>"
    exit 1
fi

output_folder="output"

# Check if the folder exists
if [ ! -d "$output_folder" ]; then
    # If not, create the folder
    mkdir "$output_folder"
    #echo "Folder '$output_folder' created."
else
    #echo "Folder '$output_folder' already exists."
fi

# Add ~/.local/bin to PATH if not already present
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    export PATH=$PATH:$HOME/.local/bin
fi

fileA="$1"
fileB="$2"
output_file="$3"  # Use the provided third argument as the output file

temp_fileA="new_$fileA"
temp_fileB="new_$fileB"

mv "$fileA" "$fileB" sys;

cd sys;

python3 parse_csv.py "$fileA" "$temp_fileA";
python3 parse_csv.py "$fileB" "$temp_fileB";
python3 compare.py "$temp_fileA" "$temp_fileB" > new_output.csv;
python3 delCol.py new_output.csv "$output_file";
python3 extract_vpr.py "$temp_fileB" "$temp_fileB".json;
python3 csv2json.py "$output_file" "$output_file".json;
python3 update_vpr.py "$temp_fileB".json "$output_file".json "$output_file".json;
python3 json2csv.py "$output_file".json "$output_file";



# Check if csvtotable is installed
if ! command -v csvtotable &> /dev/null; then
    # If not installed, try installing it using pip
    if command -v pip &> /dev/null; then
        pip install --upgrade csvtotable
    elif command -v pip3 &> /dev/null; then
        pip3 install --upgrade csvtotable
    else
        echo "Error: pip not found. Please install pip and try again."
        exit 1
    fi
fi

# Convert CSV to HTML using csvtotable
csvtotable "$output_file" "$output_file.html"

mv "$output_file" "$output_file.html" ../output

# Remove temporary files
rm *.json *.csv
