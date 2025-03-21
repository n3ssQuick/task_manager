# task_manager/core.py
import json
import os
from task_manager.logger import setup_logger
from task_manager.config import get_tasks_file_path, ensure_tasks_file_exists

logger = setup_logger()


def load_tasks():
  """Load tasks from the JSON file"""
  ensure_tasks_file_exists()
  tasks_file = get_tasks_file_path()

  try:
    with open(tasks_file, 'r') as f:
      return json.load(f)
  except json.JSONDecodeError:
    logger.error(f"Error decoding JSON from {tasks_file}")
    return []
  except Exception as e:
    logger.error(f"Error loading tasks: {str(e)}")
    return []


def save_tasks(tasks):
  """Save tasks to the JSON file"""
  tasks_file = get_tasks_file_path()

  try:
    with open(tasks_file, 'w') as f:
      json.dump(tasks, f, indent=2)
    logger.info(f"Tasks saved to {tasks_file}")
    return True
  except Exception as e:
    logger.error(f"Error saving tasks: {str(e)}")
    return False


def add_task(description, priority="medium"):
  """Add a new task to the task list"""
  tasks = load_tasks()

  # Generate a new task ID
  task_id = 1
  if tasks:
    task_id = max(task["id"] for task in tasks) + 1

  # Create new task
  new_task = {
      "id": task_id,
      "description": description,
      "priority": priority,
      "completed": False
  }

  tasks.append(new_task)

  if save_tasks(tasks):
    logger.info(f"Task added: {description} (ID: {task_id})")
    return task_id
  return None


def list_tasks():
  """List all tasks"""
  tasks = load_tasks()
  logger.info(f"Retrieved {len(tasks)} tasks")
  return tasks


def delete_task(task_id):
  """Delete a task by ID"""
  tasks = load_tasks()
  task_id = int(task_id)  # Ensure task_id is an integer

  # Find the task with the given ID
  for i, task in enumerate(tasks):
    if task["id"] == task_id:
      deleted_task = tasks.pop(i)
      if save_tasks(tasks):
        logger.info(f"Task deleted: {deleted_task['description']} (ID: {task_id})")
        return True
      return False

  logger.warning(f"Task with ID {task_id} not found")
  return False
