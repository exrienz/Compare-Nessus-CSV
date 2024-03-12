#!/bin/bash


folders=("output" "scan_output" "input" "input/prod/1" "input/prod/2" "input/prod/3" "input/nonprod/1" "input/nonprod/2" "input/nonprod/3")

for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
        #echo "Created folder: $folder"
    else
        #echo "Folder already exists: $folder"
    fi
done


echo " "
echo "Which function to choose?"
echo "1. Compare 2 Nessus Scan"
echo "2. Create a monthly RTF Deck"
echo " "
echo " "
read -p "Enter your choice (1 or 2): " user_choice

case $user_choice in
    1)
        read -p "Enter the path of the old CSV file: " old_csv_file
        read -p "Enter the path of the new CSV file: " new_csv_file
        read -p "Enter the desired result name: " result_name

        # Execute choice 1
        echo " "
		bash compare_scan.sh "$old_csv_file" "$new_csv_file" "$result_name"
        ;;
    2)
        read -p "Enter the result name for the RTF Deck: " result_name

        # Execute choice 2
        echo " "
		bash rtf.sh | tee "$result_name".txt;
		sed -i '/Parsing\|JSON cleaned successfully in\|Duplicates removed successfully\./d' "$result_name".txt;
        ;;
    *)
        echo "Invalid choice. Please enter 1 or 2."
        ;;
esac
