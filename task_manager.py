from task import Task
from task_repository import TaskRepository
import logging

logger = logging.getLogger(__name__)


class TaskManager:
    def __init__(self):
        self.repo = TaskRepository()

    def add_task(self, title, description):
        task = Task(title, description)
        self.repo.add_task(task)

    def list_tasks(self):
        return self.repo.get_all_tasks()

    def complete_task(self, task_id):
        self.repo.complete_task(task_id)

    def delete_task(self, task_id):
        self.repo.delete_task(task_id)
