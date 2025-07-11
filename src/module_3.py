import json
from pathlib import Path

class TaskListError(Exception):
    """Custom exception for task list errors."""
    pass


def list_tasks(json_file_path: str) -> str:
    """
    Reads tasks from a JSON file and returns a formatted string listing all tasks.

    Args:
        json_file_path (str): Path to the JSON file containing tasks.

    Returns:
        str: Formatted string of tasks.

    Raises:
        TaskListError: If file not found, JSON is invalid, or tasks data is malformed.
    """
    path = Path(json_file_path)

    if not path.exists():
        raise TaskListError(f"File not found: {json_file_path}")

    try:
        with path.open('r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise TaskListError(f"Invalid JSON format in file: {json_file_path}") from e

    if not isinstance(data, list):
        raise TaskListError(f"Expected a list of tasks in the JSON file, got {type(data).__name__}")

    if not data:
        return "No tasks found."

    lines = []
    for idx, task in enumerate(data, start=1):
        if not isinstance(task, dict):
            raise TaskListError(f"Task at index {idx} is not a JSON object.")

        title = task.get('title')
        completed = task.get('completed')

        if title is None or not isinstance(title, str):
            raise TaskListError(f"Task at index {idx} missing valid 'title' field.")

        if completed is None or not isinstance(completed, bool):
            raise TaskListError(f"Task at index {idx} missing valid 'completed' field.")

        status = '\u2713' if completed else '\u2717'
        lines.append(f"{idx}. [{status}] {title}")

    return "\n".join(lines)