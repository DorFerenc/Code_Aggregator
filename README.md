# Code Aggregator

## Description

Code Aggregator is a Python script that compiles all the code files from a project into a single output file. This tool is particularly useful for creating a comprehensive view of your project, which can be easily shared with AI language models for code review, debugging, or analysis.

## Features

- Recursively scans a specified project directory
- Aggregates code from various file types, including:
  - Common programming languages (.py, .js, .java, .cpp, .h, .c, .go, .rs)
  - Web development files (.html, .css)
  - Configuration files (.yml, .yaml, .json, .xml)
  - Documentation files (.md, .txt)
  - Docker-related files (Dockerfile, .dockerignore, docker-compose.yml)
- Preserves file paths relative to the project root
- Adds clear separators between files for easy navigation
- Handles potential encoding issues by using UTF-8
- Includes a timestamp for version tracking
- Respects .gitignore rules and common ignore patterns
- Automatically generates a unique output file name

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download the `code_aggregator.py` file.
2. Ensure you have Python 3.6 or higher installed on your system.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `code_aggregator.py`.
3. Run the script:

```
python code_aggregator.py
```

4. When prompted, enter the path to your project directory.
5. The script will generate an output file in the same directory as the script, with a name like

```aggregated_code_YYYYMMDD_HHMMSS.txt```

## Example

```
$ python code_aggregator.py
Enter the path to your project: /path/to/your/project
Code aggregation complete. Output written to: /path/to/script/directory/aggregated_code_20240914_153010.txt
```

## Customization

You can easily customize the types of files included in the aggregation by modifying the `code_extensions` and `docker_files` lists in the script.

## Contributing

Contributions to improve the Code Aggregator are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contact

If you have any questions, issues, or suggestions, please open an issue in this repository.

