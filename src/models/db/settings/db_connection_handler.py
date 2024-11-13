import sqlite3
from sqlite3 import Connection


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"

    def __connect(self) -> Connection:
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        return conn

    def get_connection(self) -> Connection:
        return self.__connect()


db_connection_handler = DbConnectionHandler()
