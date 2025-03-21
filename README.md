# Advanced CLI Task Manager

A command-line task manager with advanced features including subcommands, environment variables, logging, and configuration files.

## Features

- Add, list, and delete tasks
- Tasks stored in a JSON file
- Subcommands using argparse
- Logging of all actions
- Environment variable support
- Unit tests

## Installation

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Adding a task

You can add a task with a description and an optional priority level:

```bash
python -m task_manager.cli add "Complete project" --priority high
```

> Note: The priority can be `low`, `medium`, or `high`. If not specified, it defaults to `medium`.

### Listing tasks

You can list all tasks or filter by priority:

```bash
python -m task_manager.cli list
```

### Deleting a task

```bash
python -m task_manager.cli delete 1
```

## Configuration

You can set the `TASKS_FILE_PATH` environment variable to specify a custom location for the tasks file:

```bash
export TASKS_FILE_PATH=/path/to/my/tasks.json
```

## Running Tests

```bash
pytest tests/
```
