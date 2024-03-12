#!/bin/bash

output_folder="scan_output"
sys_folder="sys"

old_json=$1
new_json=$2

process_json(){
    csvfile=$1
    output_folder=$2
        
    echo "$output_folder $csvfile";
    
    python3 "$sys_folder/parse_csv.py" "$csvfile" "$output_folder/temp_$csvfile";
    mv "$output_folder/temp_$csvfile" "$output_folder/$csvfile";
    python3 "$sys_folder/csv2json.py" "$output_folder/$csvfile" "$output_folder/$csvfile.json";
    python3 "$sys_folder/jsoncleaner.py" "$output_folder/$csvfile.json";
    python3 "$sys_folder/remove_duplicate.py" "$output_folder/$csvfile.json";
}

compare(){
    # so now we got 2 clean json file. Lets compare it. Overwrite CVE risk and vpr accordance to the latest CVE in new json
    python3 "$sys_folder/jsoncompare.py" "$1" "$2" "$3.json";
    python3 "$sys_folder/jsoncleaner.py" "$3.json";
    python3 "$sys_folder/remove_duplicate.py" "$3.json";
    python3 "$sys_folder/json2csv.py" "$3.json" "$3.csv" ;    
}

echo " "
process_json $old_json $output_folder;
process_json $new_json $output_folder;
echo " "
compare $output_folder/$old_json.json $output_folder/$new_json.json $output_folder/$3;
echo " "
python3 "$sys_folder/count_vuln.py" "$output_folder/$3.json";

#rm "$output_folder/$old_json.json" "$output_folder/$new_json.json" "$output_folder/$old_json" "$output_folder/$new_json" 
rm "$3.csv";
python3 "$sys_folder/json2csv.py" "$output_folder/$3.json" "$output_folder/$3.csv" ;
