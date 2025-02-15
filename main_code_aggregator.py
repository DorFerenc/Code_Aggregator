import os
import subprocess

def main():
    print("\nWelcome to the Code Aggregator Tool!")
    print("Select the type of aggregation you want to perform:")
    print("1. Standard Aggregation (Includes all code files)")
    print("2. Excluder Mode (Allows excluding specific files)")
    print("3. Includer Mode (Allows selecting specific files to include)")
    print("4. Depth-based Aggregation (Limit depth of aggregation)")

    choice = input("Enter your choice (1-4): ").strip()

    if choice not in {'1', '2', '3', '4'}:
        print("Invalid choice. Please restart and select a valid option.")
        return

    # project_path = input("Enter the path to your project [without quotes]: ").strip('"')
    # if not os.path.isdir(project_path):
    #     print("Invalid project path. Please restart and enter a valid directory path.")
    #     return
    project_path = ""

    if choice == '1':
        subprocess.run(["python", "code_aggregator.py", project_path])
    elif choice == '2':
        subprocess.run(["python", "code_aggregator_excluder.py", project_path])
    elif choice == '3':
        subprocess.run(["python", "code_aggregator_includer.py", project_path])
    elif choice == '4':
        subprocess.run(["python", "code_aggregator_by_depth.py", project_path])

if __name__ == "__main__":
    main()