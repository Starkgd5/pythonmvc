import sqlite3
from sqlite3 import Connection


class DbConnectionHandler:
    def __init__(self, db_name="storage.db") -> None:
        self.__connection_string = db_name
        self.__conn = None

    def __enter__(self):
        self.__conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__conn:
            self.__conn.close()

    def get_connection(self) -> Connection:
        return self.__conn


class CreateTables:
    def __init__(self, connection_handler: DbConnectionHandler) -> None:
        self.__conn = connection_handler.get_connection()

    def create_table_people(self):
        query = """
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                age INTEGER
            );
        """
        self.__execute_query(query)

    def create_table_todo(self):
        query = """
            CREATE TABLE IF NOT EXISTS todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                due_date TEXT,
                person_id INTEGER,
                FOREIGN KEY (person_id) REFERENCES people(id) ON DELETE CASCADE
            );
        """
        self.__execute_query(query)

    def __execute_query(self, query: str):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(query)
            self.__conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()


# Uso do gerenciador de contexto para criar as tabelas
with DbConnectionHandler() as db_handler:
    table_creator = CreateTables(db_handler)
    table_creator.create_table_people()  # Cria a tabela people
    table_creator.create_table_todo()  # Cria a tabela todo
