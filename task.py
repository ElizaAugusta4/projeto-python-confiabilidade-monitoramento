import logging

logger = logging.getLogger(__name__)

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Concluída" if self.completed else "Pendente"
        return f"{self.id}. {self.title} - {self.description} ({status})"
