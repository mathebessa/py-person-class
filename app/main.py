from typing import List, Dict, Union


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(
    people_data: List[Dict[str, Union[str, int]]]
) -> List[Person]:
    Person.people.clear()

    person_objects = [
        Person(person["name"], person["age"])
        for person in people_data
    ]

    for person_obj, person in zip(person_objects, people_data):
        wife_name = person.get("wife")
        if isinstance(wife_name, str) and wife_name and wife_name in Person.people:
            setattr(person_obj, "wife", Person.people[wife_name])

        husband_name = person.get("husband")
        if isinstance(husband_name, str) and husband_name and husband_name in Person.people:
            setattr(person_obj, "husband", Person.people[husband_name])

    return person_objects
