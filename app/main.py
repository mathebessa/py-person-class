from typing import List, Dict, Union, Any


class Person:
    people = {}

    def __init__(self, name: str, age: int,
                 wife_name: str = None, husband_name: str = None) -> None:
        self.name = name
        self.age = age
        self.wife_name = wife_name
        self.husband_name = husband_name
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def set_spouse(self) -> None:
        if self.wife_name and self.wife_name in Person.people:
            self.wife = Person.people[self.wife_name]
        if self.husband_name and self.husband_name in Person.people:
            self.husband = Person.people[self.husband_name]

    def __getattr__(self, name: str) -> Any:
        if name == "wife" and self.wife is None:
            return None  # Não lançar erro se não houver esposa
        if name == "husband" and self.husband is None:
            return None  # Não lançar erro se não houver marido
        return object.__getattr__(self, name)


def create_person_list(
        people_data: List[Dict[str, Union[str, int]]]) -> List[Person]:
    person_objects = {}
    for person in people_data:
        name = person["name"]
        age = person["age"]
        wife_name = person.get("wife", None)
        husband_name = person.get("husband", None)
        person_objects[name] = Person(name, age, wife_name, husband_name)

    for person in person_objects.values():
        person.set_spouse()

    return list(person_objects.values())
