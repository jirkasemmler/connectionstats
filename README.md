# connectionstats

This repository contains a Python script that can count the number of lines in a specific file of a GitHub repository for every week across the years 2023, 2024 and 2025.

## Usage

The script `weekly_line_counts.py` requires Python 3 and the `GitPython` package. Install dependencies with:

```bash
pip install gitpython
```

Run the script by providing the repository URL and the path to the file you want to inspect. Optionally specify the branch (defaults to `main`). Add `--csv` to save the results to a CSV file instead of printing them to the console.

```bash
python weekly_line_counts.py <repo_url> <path/to/file> [--branch BRANCH] [--csv output.csv]
```

Without `--csv`, the output will list dates (one per week) and the corresponding number of lines in the chosen file at that point in the repository history.
