from typing import List, Dict, Union


class Person:
    people = {}

    def __init__(self, name: str, age: int, wife_name: str = None, husband_name: str = None) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

        if wife_name and wife_name in Person.people:
            self.wife = Person.people[wife_name]
        if husband_name and husband_name in Person.people:
            self.husband = Person.people[husband_name]

    def set_spouse(self) -> None:
        pass


def create_person_list(people_data: List[Dict[str, Union[str, int]]]) -> List[Person]:
    person_objects = []
    for person in people_data:
        name = person["name"]
        age = person["age"]
        wife_name = person.get("wife", None)
        husband_name = person.get("husband", None)

        person_obj = Person(name, age, wife_name, husband_name)
        person_objects.append(person_obj)

    return person_objects
