import sys
import csv

def compare_files(fileA, fileB):
    with open(fileA, 'r') as csv_fileA, open(fileB, 'r') as csv_fileB:
        readerA = csv.DictReader(csv_fileA)
        readerB = csv.DictReader(csv_fileB)

        fieldnames = readerA.fieldnames

        rowsA = {tuple(str(val) for val in row.values()) for row in readerA}
        rowsB = {tuple(str(val) for val in row.values()) for row in readerB}

        common_rows = rowsA.intersection(rowsB)
        new_rows = rowsB - common_rows
        closed_rows = rowsA - common_rows

        print("Status," + ",".join(fieldnames))
        for row in closed_rows:
            print("Closed," + ",".join(str(val) for val in row))
        for row in common_rows:
            print("Open," + ",".join(str(val) for val in row))
        for row in new_rows:
            print("New," + ",".join(str(val) for val in row))

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python compare.py old.csv new.csv")
    else:
        fileA = sys.argv[1]
        fileB = sys.argv[2]
        compare_files(fileA, fileB)
