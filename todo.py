import argparse

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

    parser.print_help()

if __name__ == "__main__":
    main()