# task_manager/config.py
import os
import json


def get_tasks_file_path():
  """Get the tasks file path from environment variable or use default"""
  return os.getenv("TASKS_FILE_PATH", "tasks.json")


def ensure_tasks_file_exists():
  """Ensure the tasks file exists, create it if it doesn't"""
  tasks_file = get_tasks_file_path()
  if not os.path.exists(tasks_file):
    with open(tasks_file, 'w') as f:
      json.dump([], f)
