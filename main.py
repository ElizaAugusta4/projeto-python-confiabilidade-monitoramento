import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from task_manager import TaskManager

# Configuração do Sentry 
sentry_sdk.init(
    dsn='https://2de99cfcea454e417e1a66704a0b7944@o4505646715371520.ingest.sentry.io/4505646722711552',
    integrations=[FlaskIntegration()]
)

def format_task(task):
    status = "Concluída" if task.completed else "Pendente"
    return f"{task.id}. {task.title} - {task.description} ({status})"

def main():
    task_manager = TaskManager()

    try:
        while True:
            print("\n=== Gerenciador de Tarefas ===")
            print("1. Adicionar Tarefa")
            print("2. Listar Tarefas")
            print("3. Concluir Tarefa")
            print("4. Excluir Tarefa")
            print("5. Sair")

            choice = input("Escolha uma opção (1-5): ")

            if choice == '1':
                title = input("Título da tarefa: ")
                description = input("Descrição da tarefa: ")
                task_manager.add_task(title, description)
                print("Tarefa adicionada com sucesso!")

            elif choice == '2':
                tasks = task_manager.list_tasks()
                print("\nLista de Tarefas:")
                for task in tasks:
                    print(task)

            elif choice == '3':
                try:
                    task_id = int(input("Digite o ID da tarefa a concluir: "))
                    task_manager.complete_task(task_id)
                    print("Tarefa concluída com sucesso!")
                except ValueError:
                    print("ID inválido. O ID da tarefa deve ser um número inteiro.")

            elif choice == '4':
                try:
                    task_id = int(input("Digite o ID da tarefa a excluir: "))
                    task_manager.delete_task(task_id)
                    print("Tarefa excluída com sucesso!")
                except ValueError:
                    print("ID inválido. O ID da tarefa deve ser um número inteiro.")

            elif choice == '5':
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")

    except Exception as e:
        # Captura exceções não tratadas e envia ao Sentry
        sentry_sdk.capture_exception(e)
        print("Ocorreu um erro inesperado. Verifique o log para mais detalhes.")
        
if __name__ == "__main__":
    main()

