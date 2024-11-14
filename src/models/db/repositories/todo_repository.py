from datetime import datetime
from src.models.db.settings.db_connection_handler import db_connection_handler


class TodoRepository:
    def __init__(self) -> None:
        self.__conn = db_connection_handler.get_connection()

    def get_todo_by_task(self, task: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute("SELECT * FROM todo WHERE task = ?", (task,))
        todo = cursor.fetchone()
        return todo

    def registry_todo(self, task: str, person_name: str) -> None:
        status = "em andamento"
        due_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor = self.__conn.cursor()
        cursor.execute("SELECT name FROM people WHERE name = ?", (person_name,))
        person = cursor.fetchone()

        cursor.execute(
            """
            INSERT INTO todo (task, status, due_date, person_id)
            VALUES (?, ?, ?, ?)""",
            (task, status, due_date, person[0]),
        )
        self.__conn.commit()
