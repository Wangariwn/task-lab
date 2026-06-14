from task_manager.task_utils import (
	add_task,
	mark_task_as_complete,
	view_pending_tasks,
	calculate_progress,
	tasks,
)


def main():
	while True:
		print("\nTask Management System")
		print("1. Add Task")
		print("2. Mark Task as Complete")
		print("3. View Pending Tasks")
		print("4. View Progress")
		print("5. Exit")
		choice = input("Enter your choice (1-5): ").strip()

		if choice == "1":
			title = input("Title: ")
			description = input("Description (optional): ")
			due_date = input("Due date (YYYY-MM-DD): ")
			ok, msg = add_task(title, description, due_date)
			if ok:
				print(msg)
			else:
				print("Error:", msg)

		elif choice == "2":
			if not tasks:
				print("No tasks available.")
				continue
			for i, t in enumerate(tasks):
				status = "✓" if t["completed"] else " "
				print(f"{i}. [{status}] {t['title']} (due {t['due_date']})")
			try:
				idx = int(input("Enter task index to mark complete: "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			ok, msg = mark_task_as_complete(idx)
			if ok:
				print(msg)
			else:
				print("Error:", msg)

		elif choice == "3":
			pending = view_pending_tasks()
			if not pending:
				print("No pending tasks.")
			else:
				for i, t in pending:
					print(f"{i}. {t['title']} - due {t['due_date']}")

		elif choice == "4":
			prog = calculate_progress()
			print(f"Progress: {prog}%")

		elif choice == "5":
			print("Exiting the program...")
			break

		else:
			print("Invalid choice. Please try again.")


if __name__ == "__main__":
	main()
