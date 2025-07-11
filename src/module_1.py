import argparse

def create_parser():
    """
    Create and return the argument parser for the task CLI tool.
    Supports commands: add, list, complete, delete.
    """
    parser = argparse.ArgumentParser(prog="taskcli")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Description of the task")

    # list command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "--completed", action="store_true", help="Show only completed tasks"
    )
    list_parser.add_argument(
        "--pending", action="store_true", help="Show only pending tasks"
    )

    # complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("task_id", type=int, help="ID of the task to complete")

    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

    return parser