# LearningPython

A personal collection of Python scripts, exercises and coding practice problems organized into topic-based folders. This repository is intended as a study log and a reference for common Python techniques, algorithms and interview preparation problems.

## Contents

The repository is now organized for clarity and ease of navigation:

### Company-Focused Problems
- `CompanyProblems/Amazon/` — Amazon interview and practice problems
- `CompanyProblems/Chargebee/` — Chargebee interview and practice problems
- `CompanyProblems/ClootrackHiring/` — Clootrack interview and practice problems
- `CompanyProblems/PaytmPG/` — Paytm Payment Gateway interview and practice problems
- `CompanyProblems/CodeChef/` — CodeChef platform problems
- `CompanyProblems/HackerRank/` — HackerRank platform problems
- `CompanyProblems/Fractal/` — Fractal company problems
- `CompanyProblems/Dunzo/` — Dunzo company problems
- `CompanyProblems/TechBoost/`, `CompanyProblems/TestPress/`, `CompanyProblems/Plivo/`, `CompanyProblems/PramataTech/`, `CompanyProblems/Skuad/`, `CompanyProblems/Singular/`, `CompanyProblems/maximl labs/`, `CompanyProblems/microsoft/`, `CompanyProblems/ey/`, `CompanyProblems/kutumb/`, `CompanyProblems/SaurabhTest/` — Other company and hiring problems

### DSA Topic-Focused Problems
- `DSA/Backtracking/` — Backtracking algorithms and problems
- `DSA/DP/` — Dynamic Programming problems
- `DSA/Basic/` — Basic Python and simple DSA problems
- `DSA/CodingBlocks/` — DSA practice from Coding Blocks
- `DSA/CodingNinja/` — DSA practice from Coding Ninja

### Python Language Features & Utilities
- `PythonFeatures/Decorators/` — Decorator examples
- `PythonFeatures/Generators/` — Generator examples
- `PythonFeatures/threading/` — Threading examples
- `PythonFeatures/AdvanceFormatting/` — Advanced formatting in Python
- `PythonFeatures/DataVisualization/` — Simple plotting and visualization examples
- `PythonFeatures/BestPractices/` — Python best practices
- `PythonFeatures/ExceptionHandling/` — Exception handling examples

### Miscellaneous & Practice
- Other folders and scripts remain for exploratory work and practice sets.

(Note: This list is not exhaustive; explore the repository to see all folders and scripts.)

## Requirements

- Python 3.8+ recommended. Many scripts are plain Python and should run on modern Python 3.x interpreters.
- No global dependencies required for most files. Specific folders may include third-party requirements — check the top of each script for imports.

## Getting started

1. Clone or unzip the repository:

   git clone <repository-url>

   or if you received `Dunzo.zip` / a zip archive, unzip it and open the folder in your editor.

2. Run an example script with the Python interpreter. For example:

   python3 Basic/HelloWorld.py

3. If a script expects command-line arguments, check the file header or open it to see usage examples. Many scripts include simple `if __name__ == '__main__':` test blocks.

## How the repository is organized

- Each folder typically groups related problems or examples (e.g., `Pattern/` for pattern printing, `DP/` for dynamic programming solutions).
- Filenames are generally descriptive (for example, `FibonacciRecursion.py`, `ReverseString.py`, etc.).
- Some folders include exploratory or learning notes (temporary files named like `tempfile.txt`).

## Tips for navigating

- Use your editor or `grep`/`rg` to search for topics or functions, for example:

  grep -R "fibonacci" -n .

- Open the folders for the topic you're interested in (e.g., `Backtracking/` for backtracking problems) and run individual scripts.

## Contributing

This repository appears to be a personal learning collection. If you want to contribute:

- Open an issue describing the improvement or the bug.
- Fork the repo, make small focused changes (add tests or examples), and create a pull request with a short description.

If this is your personal folder, keep contributions to organizing files, improving README, and adding concise docstrings or usage notes in scripts.

## Style and best practices

- Prefer small, single-purpose scripts for each problem.
- Add a brief description and usage example at the top of each script.
- Add tests or simple assertions where feasible to demonstrate correctness.

## License

This repository does not include an explicit license file. If you want to share or accept contributions, consider adding an open-source license such as MIT. Add a `LICENSE` file at the repo root when ready.

## Contact / Notes

- This is a study/practice repository created for learning and interview preparation. Use and adapt the examples as needed.
- If you want, I can also:
  - generate a `requirements.txt` for folders that need external packages,
  - add a CONTRIBUTING.md,
  - or produce a per-folder index listing the main files and a one-line description.
