from datetime import datetime
from src.models.db.settings.db_connection_handler import db_connection_handler


class TodoRepository:
    def __init__(self) -> None:
        self.__conn = db_connection_handler.get_connection()

    def __execute_query(self, query: str, params: tuple = ()) -> tuple:
        """Executa uma consulta SQL e retorna os resultados."""
        cursor = self.__conn.cursor()
        cursor.execute(query, params)
        return cursor

    def get_todo_list(self) -> list[tuple]:
        """Obtém a lista de todos os TODOs com status 'created'."""
        query = "SELECT * FROM todo WHERE status = 'em andamento'"
        return self.__execute_query(query).fetchall()

    def get_todo_by_task(self, task: str) -> tuple:
        """Obtém um TODO pelo nome da tarefa."""
        query = "SELECT * FROM todo WHERE task = ?"
        return self.__execute_query(query, (task,)).fetchone()

    def get_todo_by_id(self, id: int) -> tuple:
        """Obtém um TODO pelo ID."""
        query = "SELECT * FROM todo WHERE id = ?"
        return self.__execute_query(query, (id,)).fetchone()

    def init_todo_by_id(self, id: int, task: str) -> None:
        """Atualiza uma tarefa pelo ID, marcando-a como 'initialized'."""
        query_select = "SELECT * FROM todo WHERE id = ?"
        todo = self.__execute_query(query_select, (id,)).fetchone()
        if todo:
            query_update = "UPDATE todo SET task = ?, status = ? WHERE id = ?"
            self.__execute_query(query_update, (task, "initialized", id))
            self.__conn.commit()
    
    def delete_todo_by_id(self, id: int) -> None:
        """Deleta um TODO pelo id. """
        query_delete = "DELETE FROM todo WHERE id = ?"
        self.__execute_query(query_delete, (id,))

    def registry_todo(self, task: str, person_name: str) -> None:
        """Registra uma nova tarefa no banco de dados."""
        status = "created"
        due_date = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Obtém o ID da pessoa
        query_person = "SELECT id FROM people WHERE name = ?"
        person_id = self.__execute_query(query_person, (person_name,)).fetchone()

        if person_id:
            query_insert = """
                INSERT INTO todo (task, status, due_date, person_id)
                VALUES (?, ?, ?, ?)
            """
            self.__execute_query(query_insert, (task, status, due_date, person_id[0]))
            self.__conn.commit()
