from datetime import datetime
try:
    from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
except ImportError:
    from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        return False
    if not validate_task_description(description):
        return False
    if not validate_due_date(due_date):
        return False
        
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    return True
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if len(tasks) == 0:
        print("No tasks currently")
        return False
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return False
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    if len(tasks) == 0:
        print("No tasks currently")
        return
        
    pending_tasks = [t for t in tasks if not t["completed"]]
    if len(pending_tasks) == 0:
        print("No tasks currently")
        return
        
    for i, t in enumerate(tasks):
        if not t["completed"]:
            print(f"{i + 1}. {t['title']} - {t['description']} (Due: {t['due_date']})")
    
# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        print("No tasks currently")
        return 0.0
    
    completed = sum(1 for t in tasks if t["completed"])
    progress = (completed / len(tasks)) * 100
    return progress