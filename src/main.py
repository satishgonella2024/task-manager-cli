import argparse
import json
import os

# Function to load tasks from JSON file
def load_tasks(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return []

# Function to save tasks to JSON file
def save_tasks(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(file_path, task_description):
    tasks = load_tasks(file_path)
    tasks.append({'description': task_description, 'completed': False})
    save_tasks(file_path, tasks)

# Function to list all tasks
def list_tasks(file_path):
    tasks = load_tasks(file_path)
    for idx, task in enumerate(tasks, start=1):
        status = 'X' if task['completed'] else ' '
        print(f"{idx}. [{status}] {task['description']}")

# Function to mark a task as completed
def complete_task(file_path, task_index):
    tasks = load_tasks(file_path)
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        save_tasks(file_path, tasks)
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(file_path, task_index):
    tasks = load_tasks(file_path)
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        save_tasks(file_path, tasks)
    else:
        print("Invalid task index.")

# Main function to handle CLI commands
def main():
    parser = argparse.ArgumentParser(description='Task Management CLI Tool')
    parser.add_argument('file_path', help='Path to the task file')
    parser.add_argument('command', choices=['add', 'list', 'complete', 'delete'], help='Command to execute')
    parser.add_argument('--description', help='Description of the task to add', default='')
    parser.add_argument('--index', type=int, help='Index of the task to complete or delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.file_path, args.description)
    elif args.command == 'list':
        list_tasks(args.file_path)
    elif args.command == 'complete':
        if args.index is not None:
            complete_task(args.file_path, args.index)
        else:
            print("Task index is required for the 'complete' command.")
    elif args.command == 'delete':
        if args.index is not None:
            delete_task(args.file_path, args.index)
        else:
            print("Task index is required for the 'delete' command.")

if __name__ == '__main__':
    main()