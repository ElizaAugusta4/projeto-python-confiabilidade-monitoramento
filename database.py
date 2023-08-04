import psycopg2
from psycopg2.errors import UniqueViolation

class Database:
    def __init__(self, dbname,user, password, host, port):
        
        # Estabelece a conexão com o PostgreSQL para criação do banco de dados
        dbname='banco_de_dados_tarefas'
        conn = psycopg2.connect(
            user='postgres',
            password=96536479,
            host='localhost',
            port=5432
        )
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        dbname='banco_de_dados_tarefas'
        cursor = conn.cursor()
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{dbname}'")
        exists = cursor.fetchone()
        if not exists:
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE {dbname}")
            conn.close()
        else:
            self.conn = psycopg2.connect(
                    dbname='banco_de_dados_tarefas',
                    user='postgres',
                    password=96536479,
                    host='localhost',
                    port=5432
                )
            self.create_tables()

    def create_tables(self):
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    description TEXT,
                    completed BOOLEAN NOT NULL DEFAULT FALSE
                )
                """
            )
            self.conn.commit()

    def add_task(self, title, description):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO tasks (title, description) VALUES (%s, %s)",
                    (title, description)
                )
                self.conn.commit()
            except UniqueViolation:
                # Caso ocorra violação de chave única (título repetido), tratamos o erro aqui.
                print("Erro: Título já existente. Por favor, escolha um título diferente.")

    def get_all_tasks(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks ORDER BY id")
            return cursor.fetchall()

    def complete_task(self, task_id):
        with self.conn.cursor() as cursor:
            cursor.execute("UPDATE tasks SET completed = TRUE WHERE id = %s", (task_id,))
            self.conn.commit()

    def delete_task(self, task_id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            self.conn.commit()

    def close(self):
        self.conn.close()
