# task_manager/cli.py
import argparse
import sys
from task_manager.core import add_task, list_tasks, delete_task
from task_manager.logger import setup_logger
from task_manager.config import get_tasks_file_path

logger = setup_logger()


def main():
  parser = argparse.ArgumentParser(description="CLI Task Manager")
  subparsers = parser.add_subparsers(dest="command", help="Available commands")

  # Add Task
  add_parser = subparsers.add_parser("add", help="Add a new task")
  add_parser.add_argument("description", help="Task description")
  add_parser.add_argument("--priority", "-p", choices=["low", "medium", "high"],
                          default="medium", help="Task priority (default: medium)")

  # List Tasks
  list_parser = subparsers.add_parser("list", help="List all tasks")

  # Delete Task
  delete_parser = subparsers.add_parser("delete", help="Delete a task")
  delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

  # Parse arguments
  args = parser.parse_args()

  # If no command is provided, show help
  if not args.command:
    parser.print_help()
    sys.exit(1)

  # Execute the appropriate command
  if args.command == "add":
    task_id = add_task(args.description, args.priority)
    if task_id:
      print(f"Task added with ID: {task_id}")
    else:
      print("Failed to add task")

  elif args.command == "list":
    tasks = list_tasks()
    if not tasks:
      print("No tasks found")
    else:
      print("\nID | Priority | Description")
      print("-" * 50)
      for task in tasks:
        print(f"{task['id']:2} | {task['priority']:8} | {task['description']}")
      print()

  elif args.command == "delete":
    if delete_task(args.task_id):
      print(f"Task with ID {args.task_id} deleted")
    else:
      print(f"Failed to delete task with ID {args.task_id}")


if __name__ == "__main__":
  main()
