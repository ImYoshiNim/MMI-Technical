from datetime import datetime
import random

class Task:
    """Represents a Task entity."""
    def __init__(self, title, description, due, priority, status="Pending", created_at=None, task_id=None):
        self.task_id = task_id if task_id else random.randint(100, 999)
        self.title = title
        self.description = description
        self.due_date = due
        self.priority = priority
        self.status = status
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        """Convert task object to dictionary for database storage."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at
        }