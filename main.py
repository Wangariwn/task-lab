# Import functions from task_manager.task_utils package
try:
    from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
except ImportError:
    from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
        elif choice == "2":
            # Access tasks list safely for empty check
            try:
                from task_manager.task_utils import tasks
            except ImportError:
                from task_utils import tasks
                
            if len(tasks) == 0:
                print("No tasks currently")
            else:
                try:
                    index_str = input("Enter task index to mark as complete: ")
                    index = int(index_str) - 1
                    mark_task_as_complete(index)
                except ValueError:
                    print("Invalid task index.")
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            try:
                from task_manager.task_utils import tasks
            except ImportError:
                from task_utils import tasks
                
            if len(tasks) == 0:
                print("No tasks currently")
            else:
                progress = calculate_progress()
                print(f"Progress: {progress}%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()