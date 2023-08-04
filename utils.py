import logging

logger = logging.getLogger(__name__)

def print_task_list(tasks):
    if not tasks:
        logger.info("Nenhuma tarefa encontrada.")
    else:
        logger.info("Lista de Tarefas:")
        for task in tasks:
            logger.info(str(task))
