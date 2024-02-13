# Nessus CSV File Comparator

This script is designed to compare two Nessus CSV files and generate a report in CSV format.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Nessus CSV File Comparator is a Bash script that leverages Python scripts to parse, compare, and generate a report based on two Nessus CSV files.

## Usage

```bash
./compare_nessus_csv.sh <old.csv> <new.csv>
```

- `old.csv`: The path to the old Nessus CSV file.
- `new.csv`: The path to the new Nessus CSV file.

The script generates a report (`report.csv`) that highlights the differences between the two Nessus scans.

## Dependencies

- Python 3

Ensure that the required Python scripts (`parse_csv.py`, `compare.py`, and `delCol.py`) are present in the same directory as the Bash script.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/nessus-csv-comparator.git
cd nessus-csv-comparator
```

2. Ensure the script has execution permissions:

```bash
chmod +x compare_nessus_csv.sh
```

## Examples

```bash
./compare_nessus_csv.sh old_scan.csv new_scan.csv
```

This will generate a report (`report.csv`) highlighting the differences between the old and new Nessus scans.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
```

Make sure to replace `<old.csv>` and `<new.csv>` with actual file paths in the usage section and provide the correct repository URL in the cloning section. Also, include the appropriate license file in your repository if you choose a license other than MIT.
