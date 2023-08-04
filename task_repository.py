import logging
from database import Database
from task import Task
logger = logging.getLogger(__name__)

class TaskRepository:
    def __init__(self):
        self.db = Database(dbname='banco_de_dados_tarefas', user='postgres', password='96536479', host='localhost', port='5432')

    def add_task(self, task):
        self.db.add_task(task.title, task.description)

    def get_all_tasks(self):
        rows = self.db.get_all_tasks()
        tasks = []
        for row in rows:
            task = Task(row[1], row[2])
            task.id = row[0]
            task.completed = row[3]
            tasks.append(task)
        return tasks

    def complete_task(self, task_id):
        self.db.complete_task(task_id)

    def delete_task(self, task_id):
        self.db.delete_task(task_id)

