#!/bin/bash

input_folder="input"
output_folder="output"
sys_folder="sys"

prod_one="$input_folder/prod/1/"
prod_two="$input_folder/prod/2/"
prod_three="$input_folder/prod/3/"

nonprod_one="$input_folder/nonprod/1/"
nonprod_two="$input_folder/nonprod/2/"
nonprod_three="$input_folder/nonprod/3/"

# Create folders if they don't exist
for folder in "$input_folder" "$output_folder" "$sys_folder" \
    "$input_folder/prod/1" "$input_folder/prod/2" "$input_folder/prod/3" \
    "$input_folder/nonprod/1" "$input_folder/nonprod/2" "$input_folder/nonprod/3"; do
    [ ! -d "$folder" ] && mkdir -p "$folder"
done

p1="prod1"
p2="prod2"
p3="prod3"
np1="nonprod1"
np2="nonprod2"
np3="nonprod3"

process_folder() {
    input_folder="$1" #"$input_folder/prod/1/"
    output_folder="$2" #output_folder="output"
    csv_name="$3" #p1="prod1"
    header="CVE,Risk,Host,Port,Name,Solution,VPR Score"

    [ ! -d "$input_folder" ] && { echo "Error: Input folder not found."; exit 1; }

    cat "$input_folder"/*.csv | awk '!seen[$0]++' > "$output_folder/tmp";
    grep -v "$header" "$output_folder/tmp" > "$output_folder/temp.csv";
    echo "$header" > "$output_folder/tmp";
    cat "$output_folder/temp.csv" >> "$output_folder/tmp";
    rm "$output_folder/temp.csv";
    mv "$output_folder/tmp" "$output_folder/$csv_name";
    echo "Parsing $output_folder/$csv_name done!";
}

csv2json() {
    csvfile="$1" #"$p1"
    sys_folder="$2"
    output_folder="$3"
    
    python3 "$sys_folder/parse_csv.py" "$output_folder/$csvfile" "$output_folder/temp_$csvfile";
    mv "$output_folder/temp_$csvfile" "$output_folder/$csvfile";
    python3 "$sys_folder/csv2json.py" "$output_folder/$csvfile" "$output_folder/$csvfile.json";
    python3 "$sys_folder/jsoncleaner.py" "$output_folder/$csvfile.json";
    python3 "$sys_folder/remove_duplicate.py" "$output_folder/$csvfile.json";
}

stats(){
    
    json_file_path=$1;
    scan_name=$2;

    echo " "
    echo "==================================================================================="
    echo " "
    python3 "$sys_folder/summary_stat.py" "$1" "$2"
    echo " "
    echo "-----------------------------------------------------------------------------------"
    echo " "
    python3 "$sys_folder/top_host_stat.py" "$1"
    #echo " "
    #echo "-----------------------------------------------------------------------------------"
    #echo " "
    #python3 "$sys_folder/top_crit.py" "$1"
}

compare(){
    # so now we got 2 clean json file. Lets compare it. Overwrite CVE risk and vpr accordance to the latest CVE in new json
    python3 "$sys_folder/jsoncompare.py" "$1" "$2" "$3";
    python3 "$sys_folder/jsoncleaner.py" "$3";
    python3 "$sys_folder/remove_duplicate.py" "$3";    
}



process_folder "$prod_one" "$output_folder" "$p1";
process_folder "$prod_two" "$output_folder" "$p2";
process_folder "$prod_three" "$output_folder" "$p3";
process_folder "$nonprod_one" "$output_folder" "$np1";
process_folder "$nonprod_two" "$output_folder" "$np2";
process_folder "$nonprod_three" "$output_folder" "$np3";

csv2json "$p1" "$sys_folder" "$output_folder";
csv2json "$p2" "$sys_folder" "$output_folder";
csv2json "$p3" "$sys_folder" "$output_folder";
csv2json "$np1" "$sys_folder" "$output_folder";
csv2json "$np2" "$sys_folder" "$output_folder";
csv2json "$np3" "$sys_folder" "$output_folder";

stats "$output_folder/$p1.json" "$p1";
stats "$output_folder/$np1.json" "$np1";
stats "$output_folder/$p2.json" "$p2";
stats "$output_folder/$np2.json" "$np2";
stats "$output_folder/$p3.json" "$p3";
stats "$output_folder/$np3.json" "$np3";

# Now compare the scan
# compare prod 1 vs prod 2, prod 2 vs prod 3
# compare nonprod1 vs nonprod2, nonprod2 vs nonprod3
echo " "
echo " "
compare "$output_folder/$p1.json" "$output_folder/$p2.json" "$output_folder/$p1$p2.json";
compare "$output_folder/$p2.json" "$output_folder/$p3.json" "$output_folder/$p2$p3.json";
compare "$output_folder/$np1.json" "$output_folder/$np2.json" "$output_folder/$np1$np2.json";
compare "$output_folder/$np2.json" "$output_folder/$np3.json" "$output_folder/$np2$np3.json";

# extract 2nd checkpoint prod/nonprod and 3rd checkpoint prod/nonprod
echo " "
echo " "
echo "Previous Month Stat :: ======================================================================================";
echo " "
python3 "$sys_folder/count_vuln_env.py"  "$output_folder/$p1$p2.json" "$output_folder/$np1$np2.json";
echo " "
echo "Current Month Stat :: ======================================================================================";
echo " "
python3 "$sys_folder/count_vuln_env.py" "$output_folder/$p2$p3.json" "$output_folder/$np2$np3.json";
echo " "
echo "=====================================================================================================";
