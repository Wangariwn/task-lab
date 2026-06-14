from datetime import datetime


def validate_task_title(title):
	"""Validate task title: non-empty string, max 100 chars."""
	if not isinstance(title, str) or not title.strip():
		return False, "Title must be a non-empty string."
	if len(title.strip()) > 100:
		return False, "Title must be at most 100 characters."
	return True, ""


def validate_task_description(description):
	"""Validate description: optional, if provided must be a string and not too long."""
	if description is None:
		return True, ""
	if not isinstance(description, str):
		return False, "Description must be a string."
	if len(description.strip()) > 500:
		return False, "Description must be at most 500 characters."
	return True, ""


def validate_due_date(due_date):
	"""Validate due date string in YYYY-MM-DD and not in the past."""
	if not isinstance(due_date, str) or not due_date.strip():
		return False, "Due date must be provided as YYYY-MM-DD."
	try:
		dt = datetime.strptime(due_date, "%Y-%m-%d").date()
	except ValueError:
		return False, "Due date must be in YYYY-MM-DD format."
	today = datetime.today().date()
	if dt < today:
		return False, "Due date cannot be in the past."
	return True, ""
