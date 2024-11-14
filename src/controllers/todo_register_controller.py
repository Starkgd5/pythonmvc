from src.models.db.repositories.todo_repository import TodoRepository


class TodoRegisterController:
    def __init__(self):
        self.__todo_repository = TodoRepository()

    def create_todo(self, task: str, person_name: str) -> dict:
        self.__validate_todo_registry(task)
        self.__insert_todo(task, person_name)
        response = self.__format_response(task, person_name)
        return response

    def __validate_todo_registry(self, task: str) -> None:
        todo = self.__todo_repository.get_todo_by_task(task)
        if todo:
            raise Exception("Person already registred")

    def __insert_todo(self, task: str, person_name: str) -> None:
        self.__todo_repository.registry_todo(task, person_name)

    def __format_response(self, task: str, person_name: str) -> dict:
        todo = self.__todo_repository.get_todo_by_task(task)
        return {
            "id": todo[0],
            "task": task,
            "status": todo[2],
            "due_date": todo[3],
            "person_name": person_name,
        }
