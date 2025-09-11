from typing import List, Dict, Union


class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int,
            wife_name: str = None,
            husband_name: str = None,
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
        self._wife_name = wife_name
        self._husband_name = husband_name

    def set_spouse(self) -> None:
        if self._wife_name is not None and self._wife_name in Person.people:
            setattr(self, "wife", Person.people[self._wife_name])
        if (
                self._husband_name is not None
                and self._husband_name in Person.people
        ):
            setattr(self, "husband", Person.people[self._husband_name])

        del self._wife_name
        del self._husband_name


def create_person_list(
    people_data: List[Dict[str, Union[str, int]]]
) -> List[Person]:
    person_objects = [
        Person(
            person["name"],
            person["age"],
            person.get("wife", None),
            person.get("husband", None),
        )
        for person in people_data
    ]

    for person_obj in person_objects:
        person_obj.set_spouse()

    return person_objects
