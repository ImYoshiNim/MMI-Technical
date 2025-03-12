import pymongo

class TaskManager:
    """Handles task operations and database interactions."""
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["task_manager"]
        self.tasks_collection = self.db["tasks"]

    def add(self, task):
        """Adds a new task to the database."""
        self.tasks_collection.insert_one(task.to_dict())
        print("Task added successfully!")

    def list(self, filter_by=None, sort_by=None):
        """Lists all tasks with optional filtering and sorting."""
        query = {} if not filter_by else filter_by
        tasks = self.tasks_collection.find(query)
        if sort_by:
            tasks = tasks.sort(sort_by)
        for task in tasks:
            print(f"[{task['task_id']}] {task['title']} - {task['status']} - Due: {task['due_date']} - Priority: {task['priority']}")

    def close(self):
        """Closes the database connection."""
        self.client.close()

    def update(self, task_id, updates):
        """Updates a task by ID."""
        self.tasks_collection.update_one({"task_id": task_id}, {"$set": updates})
        print("Task updated successfully!")

    def completed(self, task_id):
        """Marks a task as completed."""
        self.tasks_collection.update_one({"task_id": task_id}, {"$set": {"status": "Completed"}})
        print("Task marked as completed!")

    def delete(self, task_id):
        """Deletes a task by ID."""
        self.tasks_collection.delete_one({"task_id": task_id})
        print("Task deleted successfully!")