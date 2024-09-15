import os
import datetime
import fnmatch
from collections import Counter

def should_ignore(path, ignore_patterns):
    """Check if the path should be ignored based on gitignore patterns."""
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def read_gitignore(project_path):
    """Read .gitignore file and return a list of patterns to ignore."""
    gitignore_path = os.path.join(project_path, '.gitignore')
    ignore_patterns = [
        'venv', 'venv/*', '.venv', '.venv/*',  # Virtual environment
        '.idea', '.idea/*',  # PyCharm files
        '*cache*', '*.pyc', '__pycache__', '*.class', '*.o',
        '.git', '.gitignore', '*.exe'  # Common ignore patterns
    ]
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as gitignore_file:  # Renamed the file object to 'gitignore_file'
            for line in gitignore_file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    return ignore_patterns

def generate_project_structure(project_path, ignore_patterns, exclude_list=None):
    """Generate a string representation of the project structure, excluding certain files."""
    structure = []
    project_name = os.path.basename(project_path)
    file_list = []

    def add_to_structure(path, prefix=''):
        files = sorted(os.listdir(path))
        pointers = ['├──'] * (len(files) - 1) + ['└──']
        for pointer, name in zip(pointers, files):
            full_path = os.path.join(path, name)
            rel_path = os.path.relpath(full_path, project_path)
            if should_ignore(rel_path, ignore_patterns) or (exclude_list and rel_path in exclude_list):
                continue
            structure.append(f'{prefix}{pointer} {name}')
            file_list.append(rel_path)
            if os.path.isdir(full_path):
                add_to_structure(full_path, prefix + ('│   ' if pointer == '├──' else '    '))

    structure.append(project_name + '/')
    add_to_structure(project_path)
    return '\n'.join(structure), file_list

def aggregate_code(project_path, output_file, exclude_list):
    """Aggregate code and write it to the output file, excluding files in the exclude_list."""
    code_extensions = [
        '.py', '.js', '.html', '.css', '.java', '.cpp', '.h', '.c', '.go', '.rs',
        '.yml', '.yaml', '.json', '.xml', '.md', '.txt'
    ]
    docker_files = ['Dockerfile', '.dockerignore', 'docker-compose.yml', 'docker-compose.yaml']

    ignore_patterns = read_gitignore(project_path)

    file_counter = Counter()
    total_files = 0

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(f"Project Code Aggregation\n")
            outfile.write(f"Generated on: {datetime.datetime.now()}\n\n")

            # Generate and write the structure based on non-excluded files
            outfile.write("Project Structure (Excluding Selected Files):\n")
            outfile.write("==================\n")
            structure, _ = generate_project_structure(project_path, ignore_patterns, exclude_list)
            outfile.write(structure)
            outfile.write("\n\n")

            outfile.write("File Contents:\n")
            outfile.write("==============\n\n")

            for root, dirs, files in os.walk(project_path):
                dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]

                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, project_path)

                    if should_ignore(relative_path, ignore_patterns) or relative_path in exclude_list:
                        continue

                    if any(file.endswith(ext) for ext in code_extensions) or file in docker_files:
                        outfile.write(f"{'='*80}\n")
                        outfile.write(f"File: {relative_path}\n")
                        outfile.write(f"{'='*80}\n\n")

                        try:
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                                outfile.write(content)

                            file_ext = os.path.splitext(file)[1] or file
                            file_counter[file_ext] += 1
                            total_files += 1
                        except Exception as e:
                            outfile.write(f"Error reading file: {str(e)}\n")
                        outfile.write("\n\n")

            outfile.write(f"{'='*80}\n")
            outfile.write("Summary:\n")
            outfile.write(f"{'='*80}\n\n")
            outfile.write(f"Total files processed: {total_files}\n\n")
            outfile.write("Files by type:\n")
            for file_type, count in file_counter.most_common():
                outfile.write(f"  {file_type}: {count}\n")

        print(f"Code aggregation complete. Output written to: {os.path.abspath(output_file)}")
    except IOError as e:
        print(f"Error: Unable to write to the output file. {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Usage
if __name__ == "__main__":
    while True:
        project_path = input("Enter the path to your project [without quotes]: ").strip('"')
        if os.path.isdir(project_path):
            break
        else:
            print("Invalid project path. Please enter a valid directory path.")

    output_file = f"aggregated_code_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    ignore_patterns = read_gitignore(project_path)

    # Step 1: Generate and display project structure and summary
    print("Generating project structure and summary...")
    structure, file_list = generate_project_structure(project_path, ignore_patterns)
    print(structure)

    # Step 2: Display summary of files
    print("\nSummary of files:")
    for idx, file in enumerate(file_list, 1):
        print(f"{idx}: {file}")

    # Step 3: Allow user to exclude files
    exclude_list = []
    while True:
        exclude_input = input("Enter the numbers of files to exclude (comma-separated, or 'done' to finish): ").strip()
        if exclude_input.lower() == 'done':
            break
        try:
            exclude_indices = [int(i) - 1 for i in exclude_input.split(',') if i.strip().isdigit()]
            exclude_list = [file_list[i] for i in exclude_indices if 0 <= i < len(file_list)]
            print(f"Files excluded: {', '.join(exclude_list)}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # Step 4: Generate the final output without the excluded files and structure
    aggregate_code(project_path, output_file, exclude_list)
