import argparse
import json
import os
import sys

def get_data_file():
    """Gets the path to the data file, relative to the script's location."""
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))  # Directory of the script
    return os.path.join(script_dir, "todo_list.json")  # File in the same directory

def load_tasks():
    """Loads tasks from the data file."""
    data_file = get_data_file()  # Get the file path
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Saves tasks to the data file."""
    data_file = get_data_file() # Get the file path
    with open(data_file, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    """Adds a new task."""
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task added: {description}")

def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description="Command line TODO list app.")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Subparser for adding a task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")

    # Subparser for listing tasks
    list_parser = subparsers.add_parser("list", help="List all tasks")

    # Subparser for completing a task
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("task_number", type=int, help="Number of the task to complete")

    # Subparser for deleting a task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_number", type=int, help="Number of the task to delete")

    #Subparser for clearing all tasks
    clear_parser = subparsers.add_parser("clear", help="Clear all tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.task_number)
    elif args.command == "delete":
        delete_task(args.task_number)
    elif args.command == "clear":
        clear_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()