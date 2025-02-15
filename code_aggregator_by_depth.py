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
        with open(gitignore_path, 'r') as gitignore_file:
            for line in gitignore_file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    return ignore_patterns

def generate_project_structure(project_path, ignore_patterns, max_depth):
    """Generate a string representation of the project structure with depth limit."""
    structure = []
    project_name = os.path.basename(project_path)

    def add_to_structure(path, prefix='', current_depth=0):
        if current_depth > max_depth:
            return
        try:
            files = sorted([f for f in os.listdir(path) if not os.path.islink(os.path.join(path, f))])
        except PermissionError:
            return
        pointers = ['├──'] * (len(files) - 1) + ['└──']
        for pointer, name in zip(pointers, files):
            full_path = os.path.join(path, name)
            rel_path = os.path.relpath(full_path, project_path)
            if should_ignore(rel_path, ignore_patterns):
                continue
            structure.append(f'{prefix}{pointer} {name}')
            if os.path.isdir(full_path):
                add_to_structure(full_path, prefix + ('│   ' if pointer == '├──' else '    '), current_depth + 1)

    structure.append(project_name + '/')
    add_to_structure(project_path, '', 0)
    return '\n'.join(structure)

def aggregate_code(project_path, output_file, max_depth):
    code_extensions = [
        '.py', '.js', '.html', '.css', '.java', '.cpp', '.h', '.c', '.go', '.rs',
        '.yml', '.yaml', '.json', '.xml', '.md', '.txt', '.dart', '.kt', '.swift', '.php', '.java', '.rb'
    ]
    docker_files = ['Dockerfile', '.dockerignore', 'docker-compose.yml', 'docker-compose.yaml']

    ignore_patterns = read_gitignore(project_path)
    file_counter = Counter()
    total_files = 0

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(f"Project Code Aggregation\n")
            outfile.write(f"Generated on: {datetime.datetime.now()}\n\n")

            outfile.write("Project Structure:\n")
            outfile.write("==================\n")
            structure = generate_project_structure(project_path, ignore_patterns, max_depth)
            outfile.write(structure)
            outfile.write("\n\n")

            outfile.write("File Contents:\n")
            outfile.write("==============\n\n")

            for root, dirs, files in os.walk(project_path):
                depth = root[len(project_path):].count(os.sep)
                if depth > max_depth:
                    continue
                dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]

                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, project_path)

                    if should_ignore(relative_path, ignore_patterns):
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

if __name__ == "__main__":
    while True:
        project_path = input("Enter the path to your project [without quotes]: ").strip('"')
        if os.path.isdir(project_path):
            break
        else:
            print("Invalid project path. Please enter a valid directory path.")

    while True:
        try:
            max_depth = int(input("Enter the maximum depth to aggregate (0 for root only, -1 for no limit): "))
            if max_depth >= -1:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    output_file = f"aggregated_code_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    aggregate_code(project_path, output_file, max_depth)
