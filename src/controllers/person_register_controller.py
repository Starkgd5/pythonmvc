class PersonRegisterController:
    def create_person(self, name: str, age: int) -> dict:
        self.__validate_person_registry(name)
        self.__insert_person(name, age)
        response = self.__format_response(name)
        return response

    def __validate_person_registry(self, name: str) -> None:
        person = None
        if person:
            raise Exception("Person already registred")

    def __insert_person(self, name: str, age: int) -> None:
        pass

    def __format_response(self, name: str) -> dict:
        return {"id": 1, "name": name}
