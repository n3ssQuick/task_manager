import unittest
import os
import json
import tempfile
from task_manager.core import add_task, delete_task, load_tasks
from task_manager.logger import setup_logger


logger = setup_logger(log_file="test_task_manager.log")


class TestTaskManager(unittest.TestCase):
  def setUp(self):
    """Set up a temporary tasks file for testing"""
    self.temp_dir = tempfile.TemporaryDirectory()
    self.tasks_file = os.path.join(self.temp_dir.name, "test_tasks.json")
    os.environ["TASKS_FILE_PATH"] = self.tasks_file

    # Initialize with empty tasks
    with open(self.tasks_file, 'w') as f:
      json.dump([], f)
    logger.info("Set up temporary tasks file for testing")

  def tearDown(self):
    """Clean up after tests"""
    self.temp_dir.cleanup()
    if "TASKS_FILE_PATH" in os.environ:
      del os.environ["TASKS_FILE_PATH"]
    logger.info("Cleaned up after tests")

  def test_add_task(self):
    """Test adding a task"""
    logger.info("Starting test_add_task")
    # Add a task
    task_id = add_task("Test task", "high")
    logger.info(f"Added task with ID: {task_id}")

    # Verify task was added
    self.assertIsNotNone(task_id)

    # Check if task exists in the file
    tasks = load_tasks()
    self.assertEqual(len(tasks), 1)
    self.assertEqual(tasks[0]["description"], "Test task")
    self.assertEqual(tasks[0]["priority"], "high")
    self.assertEqual(tasks[0]["id"], task_id)
    logger.info("test_add_task passed")

  def test_delete_task(self):
    """Test deleting a task"""
    logger.info("Starting test_delete_task")
    # Add a task first
    task_id = add_task("Task to delete")
    logger.info(f"Added task with ID: {task_id}")

    # Verify task was added
    tasks = load_tasks()
    self.assertEqual(len(tasks), 1)

    # Delete the task
    result = delete_task(task_id)
    logger.info(f"Deleted task with ID: {task_id}, result: {result}")

    # Verify deletion was successful
    self.assertTrue(result)

    # Check if task was removed
    tasks = load_tasks()
    self.assertEqual(len(tasks), 0)
    logger.info("test_delete_task passed")

  def test_delete_nonexistent_task(self):
    """Test deleting a task that doesn't exist"""
    logger.info("Starting test_delete_nonexistent_task")
    # Try to delete a task that doesn't exist
    result = delete_task(999)
    logger.info(f"Tried to delete nonexistent task with ID: 999, result: {result}")

    # Verify deletion failed
    self.assertFalse(result)
    logger.info("test_delete_nonexistent_task passed")


if __name__ == "__main__":
  unittest.main()
