import os
import datetime
import fnmatch

def should_ignore(path, ignore_patterns):
    """Check if the path should be ignored based on gitignore patterns."""
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def read_gitignore(project_path):
    """Read .gitignore file and return a list of patterns to ignore."""
    gitignore_path = os.path.join(project_path, '.gitignore')
    ignore_patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as gitignore_file:
            for line in gitignore_file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    return ignore_patterns

def aggregate_code(project_path, output_file):
    # Define the file extensions and names we want to include
    code_extensions = [
        '.py', '.js', '.html', '.css', '.java', '.cpp', '.h', '.c', '.go', '.rs',
        '.yml', '.yaml', '.json', '.xml', '.md', '.txt'  # Configuration and documentation files
    ]
    docker_files = ['Dockerfile', '.dockerignore', 'docker-compose.yml', 'docker-compose.yaml']

    ignore_patterns = read_gitignore(project_path)
    ignore_patterns.extend(['*cache*', '*.pyc', '__pycache__', '*.class', '*.o'])  # Common ignore patterns

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Write a header with timestamp
            outfile.write(f"Project Code Aggregation\n")
            outfile.write(f"Generated on: {datetime.datetime.now()}\n\n")

            # Walk through the project directory
            for root, dirs, files in os.walk(project_path):
                # Remove directories that should be ignored
                dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]

                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, project_path)

                    # Skip files that should be ignored
                    if should_ignore(relative_path, ignore_patterns):
                        continue

                    # Check if the file is a code file or a Docker-related file
                    if any(file.endswith(ext) for ext in code_extensions) or file in docker_files:
                        # Write file information
                        outfile.write(f"{'='*80}\n")
                        outfile.write(f"File: {relative_path}\n")
                        outfile.write(f"{'='*80}\n\n")

                        # Read and write file contents
                        try:
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                                outfile.write(content)
                        except Exception as e:
                            outfile.write(f"Error reading file: {str(e)}\n")

                        outfile.write("\n\n")

        print(f"Code aggregation complete. Output written to: {os.path.abspath(output_file)}")
    except IOError as e:
        print(f"Error: Unable to write to the output file. {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Usage
if __name__ == "__main__":
    while True:
        project_path = input("Enter the path to your project: ").strip('"')
        if os.path.isdir(project_path):
            break
        else:
            print("Invalid project path. Please enter a valid directory path.")

    output_file = f"aggregated_code_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    aggregate_code(project_path, output_file)