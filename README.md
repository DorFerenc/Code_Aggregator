# Code Aggregator 📚🔍

Easily compile your entire project into a single, AI-friendly file!

## Quick Start 🚀

```bash
# Clone the repository
git clone https://github.com/yourusername/code-aggregator.git
cd code-aggregator

# Run the script
python code_aggregator.py

# Enter your project path when prompted
Enter the path to your project: /path/to/your/project

# Output will be generated in the current directory
Code aggregation complete. Output written to: /path/to/code-aggregator/aggregated_code_20240914_153010.txt
```

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

## Description 📝

Code Aggregator is a Python script that compiles all the code files from a project into a single output file. It's perfect for:

- Sharing your entire project with AI language models 🤖
- Quick code reviews 👀
- Project structure analysis 🏗️
- Debugging assistance 🐛

## Features ✨

- 🌳 Generates a visual project structure
- 📂 Recursively scans directories
- 🧩 Aggregates various file types (Python, JavaScript, HTML, CSS, etc.)
- 🏷️ Preserves relative file paths
- 🚫 Respects .gitignore rules
- 🕰️ Includes timestamp for tracking
- 📊 Provides a summary of processed files

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
   python code_aggregator.py
   ```
4. Enter your project's path when prompted
5. Find the output file in the same directory as the script

## Customization 🛠️

Modify `code_extensions` and `docker_files` in the script to customize included file types.

## Contributing 🤝

Contributions are welcome! Feel free to submit a Pull Request.

## License 📜

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contact 📫

Questions or suggestions? Open an issue in this repository!