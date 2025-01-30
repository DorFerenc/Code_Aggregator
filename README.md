# Code Aggregator 📚🔍

Easily compile your entire project into a single, AI-friendly file!

## Quick Start 🚀

```bash
# Clone the repository
git clone https://github.com/yourusername/code-aggregator.git
cd code-aggregator

# Run the main aggregator script
python main_code_aggregator.py
```

## Aggregation Modes 🏗️

When you run `main_code_aggregator.py`, you'll be prompted to choose an aggregation mode:

1. **Standard Aggregation** (`code_aggregator.py`): Compiles all code files in the project into a single output file.
2. **Excluder Mode** (`code_aggregator_excluder.py`): Allows you to exclude specific files before aggregation.
3. **Includer Mode** (`code_aggregator_includer.py`): Lets you select only specific files to be included in the aggregation.
4. **Depth-based Aggregation** (`code_aggregator_by_depth.py`): Aggregates files up to a specified depth in the directory tree.

## Output Example 📄

The generated file will look something like this:

```
Project Code Aggregation
Generated on: 2024-09-14 15:30:10

Project Structure:
==================
your-project/
├── app/
│   ├── models/
│   │   └── user.py
│   ├── services/
│   │   └── auth_service.py
│   └── main.py
├── tests/
│   └── test_auth.py
├── .gitignore
└── README.md

File Contents:
==============

================================================================================
File: app/models/user.py
================================================================================

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

... (content of other files) ...

================================================================================
Summary:
================================================================================

Total files processed: 5

Files by type:
  .py: 4
  .md: 1
```

## Features ✨

- 🌳 Generates a visual project structure
- 📂 Recursively scans directories
- 🧩 Aggregates various file types (Python, JavaScript, HTML, CSS, etc.)
- 🏷️ Preserves relative file paths
- 🚫 Respects .gitignore rules
- 🕰️ Includes timestamp for tracking
- 📊 Provides a summary of processed files
- 🗂️ Multiple aggregation modes for full control over included content

## Requirements 🛠️

- Python 3.6 or higher

## Installation 💽

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/code-aggregator.git
   ```
2. Navigate to the project directory:
   ```
   cd code-aggregator
   ```

## Usage 🖥️

1. Open your terminal
2. Navigate to the script's directory
3. Run:
   ```
   python main_code_aggregator.py
   ```
4. Select an aggregation mode when prompted
5. Enter your project's path when asked
6. If using `excluder` or `includer` modes, select files accordingly
7. Find the output file in the same directory as the script

## Customization 🛠️

Modify `code_extensions` and `docker_files` in the script to customize included file types.

## Contributing 🤝

Contributions are welcome! Feel free to submit a Pull Request.

## License 📜

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contact 📫

Questions or suggestions? Open an issue in this repository!