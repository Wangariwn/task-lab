from datetime import datetime
from .validations import (
	validate_task_title,
	validate_task_description,
	validate_due_date,
)

# In-memory tasks list
tasks = []


def add_task(title, description, due_date):
	"""Validate input and add a task to the tasks list.

	Returns (True, message) on success or (False, error_message) on failure.
	"""
	ok, msg = validate_task_title(title)
	if not ok:
		return False, msg
	ok, msg = validate_task_description(description)
	if not ok:
		return False, msg
	ok, msg = validate_due_date(due_date)
	if not ok:
		return False, msg

	task = {
		"title": title.strip(),
		"description": description.strip() if description else "",
		"due_date": due_date,
		"completed": False,
		"created_at": datetime.now().isoformat(),
	}
	tasks.append(task)
	return True, "Task added successfully."


def mark_task_as_complete(index, tasks_list=None):
	"""Mark task at given index as complete."""
	if tasks_list is None:
		tasks_list = tasks
	if not isinstance(index, int) or index < 0 or index >= len(tasks_list):
		return False, "Invalid task index."
	tasks_list[index]["completed"] = True
	return True, "Task marked as complete."


def view_pending_tasks(tasks_list=None):
	"""Return a list of (index, task) for pending tasks."""
	if tasks_list is None:
		tasks_list = tasks
	pending = [(i, t) for i, t in enumerate(tasks_list) if not t.get("completed")]
	return pending


def calculate_progress(tasks_list=None):
	"""Return percentage of tasks completed (rounded to 2 decimals)."""
	if tasks_list is None:
		tasks_list = tasks
	total = len(tasks_list)
	if total == 0:
		return 0.0
	completed = sum(1 for t in tasks_list if t.get("completed"))
	progress = (completed / total) * 100
	return round(progress, 2)
