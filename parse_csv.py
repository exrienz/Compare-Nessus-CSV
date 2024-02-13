import csv
import sys

def fix_solution_column(input_file, output_file):
    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.reader(csv_in, delimiter=',')
        writer = csv.writer(csv_out, delimiter=',')

        # Write header
        header = next(reader)
        writer.writerow(header)

        for row in reader:
            # Check if "Solution" column is not empty and fix line breaks
            if row[4] != 'n/a':
                row[4] = row[4].replace('\n', ' ')

            # Write the modified row to the output file
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file.csv output_file.csv")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        fix_solution_column(input_file_path, output_file_path)
