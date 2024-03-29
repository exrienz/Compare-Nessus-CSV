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

This script facilitates the comparison of two Nessus CSV outputs, identifying findings as either New, Aging, or Closed. This aids in monitoring monthly Vulnerability Assessment (VA) progress. Additionally, the script generates a three-month VA summary, ideal for Real-Time Feedback (RTF) meetings.

## Accepted Nessus CSV format
![GitHub Logo](/sys/requirement.png)


## Usage

```bash
./runner.sh
```

## Dependencies

- Python 3

Ensure that the required Python scripts (`parse_csv.py`, `compare.py`, and `delCol.py`) are present in the same directory as the Bash script.

## Installation

1. Clone the repository:

```bash
https://github.com/exrienz/Compare-Nessus-CSV.git
cd Compare-Nessus-CSV

```

2. Ensure the script has execution permissions:

```bash
chmod +x runner.sh
```

## Examples

```bash
./runner.sh
```

## Folder Structure
![GitHub Logo](/sys/structure.png)

## RTF Flow
![GitHub Logo](/sys/rtf.png)

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are welcome!

