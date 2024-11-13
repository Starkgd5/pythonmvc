from src.models.db.settings.db_connection_handler import db_connection_handler


class PeopleRepository:
    def __init__(self):
        self.__conn = db_connection_handler.get_connection()

    def get_person_by_name(self, name: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute("SELECT name, age FROM people WHERE name = ?", (name,))
        person = cursor.fetchone()
        return person

    def registry_person(self, name: str, age: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            "INSERT INTO people (name, age) VALUES (?, ?)", (name, age)
        )
        self.__conn.commit()