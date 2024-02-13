import sys
import csv

def compare_files(fileA, fileB):
    with open(fileA, 'r') as csv_fileA, open(fileB, 'r') as csv_fileB:
        readerA = csv.DictReader(csv_fileA)
        readerB = csv.DictReader(csv_fileB)

        fieldnames = readerA.fieldnames

        rowsA = {tuple(row.values()) for row in readerA}
        rowsB = {tuple(row.values()) for row in readerB}

        common_rows = rowsA.intersection(rowsB)
        new_rows = rowsB - common_rows
        closed_rows = rowsA - common_rows

        print("Status," + ",".join(fieldnames))
        for row in closed_rows:
            print("Closed," + ",".join(row))
        for row in common_rows:
            print("Open," + ",".join(row))
        for row in new_rows:
            print("New," + ",".join(row))

if __name__ == "__main__":
    # Check if the correct number of command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python compare.py old.csv new.csv")
    else:
        fileA = sys.argv[1]
        fileB = sys.argv[2]
        compare_files(fileA, fileB)

