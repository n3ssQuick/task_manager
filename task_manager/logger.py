# task_manager/logger.py
import logging
import os


def setup_logger(log_file="task_manager.log"):
  log_directory = "logs"

  # Create logs directory if it doesn't exist
  if not os.path.exists(log_directory):
    os.makedirs(log_directory)

  log_path = os.path.join(log_directory, log_file)

  # Configure logger
  logger = logging.getLogger("task_manager")
  logger.setLevel(logging.INFO)

  # File handler
  file_handler = logging.FileHandler(log_path)
  file_handler.setLevel(logging.INFO)

  # Console handler
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.INFO)

  # Formatter
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  file_handler.setFormatter(formatter)
  console_handler.setFormatter(formatter)

  # Add handlers to logger
  logger.addHandler(file_handler)
  logger.addHandler(console_handler)

  return logger
