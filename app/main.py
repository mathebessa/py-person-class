from typing import List, Dict, Union


class Person:
    people = {}

    def __init__(self, name: str, age: int, wife_name: str = None,
                 husband_name: str = None) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
        self._wife_name = wife_name
        self._husband_name = husband_name

    def set_spouse(self) -> None:
        if self._wife_name is not None:
            if self._wife_name in Person.people:
                setattr(self, "wife", Person.people[self._wife_name])
            else:
                raise AttributeError(
                    f"{self.name} has no wife named {self._wife_name}"
                )

        if self._husband_name is not None:
            if self._husband_name in Person.people:
                setattr(self, "husband", Person.people[self._husband_name])
            else:
                raise AttributeError(
                    f"{self.name} has no husband named {self._husband_name}"
                )

        del self._wife_name
        del self._husband_name


def create_person_list(
        people_data: List[Dict[str, Union[str, int]]]
) -> List[Person]:
    person_objects = []

    for person in people_data:
        name = person["name"]
        age = person["age"]
        wife_name = person.get("wife", None)
        husband_name = person.get("husband", None)

        person_obj = Person(
            name, age, wife_name,
            husband_name
        )
        person_objects.append(person_obj)

    for person_obj in person_objects:
        person_obj.set_spouse()

    return person_objects
