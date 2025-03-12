import re
from datetime import datetime
from taskmanager import TaskManager
from task import Task

class TaskRun:
    def __init__(self):
        self.manager = TaskManager()

    def main(self):
        while True:
            print("\nTaskManager\n")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Update Task")
            print("4. Mark Task as Completed")
            print("5. Delete Task")
            print("6. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add()
            elif choice == "2":
                self.list()
            elif choice == "3":
                self.update()
            elif choice == "4":
                self.completed()
            elif choice == "5":
                self.delete()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")
        
        self.manager.close()


    def add(self):
        title = input("Enter Title of Task: ")
        description = input("Enter the Description of Task: ")
        due = self.get_valid_due_date()
        priority = self.get_valid_priority()
        task = Task(title, description, due, priority)
        self.manager.add(task)

    def list(self):
        """Handles listing tasks via CLI."""
        self.manager.list()

    def update(self):
        """Handles updating a task via CLI."""
        task_id = int(input("Enter task ID to update: "))
        updates = {}

        updates["title"] = input("Enter new title (leave blank to keep current): ")
        updates["description"] = input("Enter new description (leave blank to keep current): ")
        updates["due_date"] = self.get_valid_due_date()
        updates["priority"] = self.get_valid_priority()
        updates["status"] = self.get_valid_priority

        updates = {k: v for k, v in updates.items() if v}  # Remove empty values

        if updates:
            self.manager.update(task_id, updates)
            print("Task updated successfully.")
        else:
            print("No changes made.")

    def confirm_update(self, prompt):
        """Helper function to confirm if a field should be updated."""
        return input(prompt).strip().lower() == "y"

    def completed(self):
        """Handles marking a task as completed via CLI."""
        task_id = int(input("Enter task ID to mark as completed: "))
        self.manager.completed(task_id)

    def delete(self):
        """Handles deleting a task via CLI."""
        task_id = int(input("Enter task ID to delete: "))
        self.manager.delete(task_id)

    def get_valid_due_date(self):
        while True:
            try:
                year = int(input("Enter due year (YYYY): "))
                if year < datetime.today().year:
                    print("Year cannot be in the past.")
                    continue
                month = int(input("Enter due month (1-12): "))
                if month < 1 or month > 12:
                    print("Invalid month. Please enter a value between 1 and 12.")
                    continue
                day = int(input("Enter due day (1-31): "))
                due_date = datetime(year, month, day).strftime("%Y-%m-%d")
                return due_date
            except ValueError:
                print("Invalid input. Please enter a valid year, month, and day.")

    def get_valid_priority(self):
            while True:
                priority = input("Enter level of priority (Low, Medium, High): ").strip().capitalize()
                if priority in ["Low", "Medium", "High"]:
                    return priority
                print("Invalid input. Please enter 'Low', 'Medium', or 'High'.")

    def get_valid_status(self):
        while True:
            status = input("Enter task status (Pending, In Progress, Completed): ").strip().capitalize()
            if status in ["Pending", "In Progress", "Completed"]:
                return status
            print("Invalid input. Please enter 'Pending', 'In Progress', or 'Completed'.")