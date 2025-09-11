from typing import List, Dict, Union


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(
        self,
        wife_name: Union[str, None] = None,
        husband_name: Union[str, None] = None,
    ) -> None:
        if wife_name is not None and wife_name != "":
            spouse = Person.people.get(wife_name)
            if spouse:
                object.__setattr__(self, "wife", spouse)

        if husband_name is not None and husband_name != "":
            spouse = Person.people.get(husband_name)
            if spouse:
                object.__setattr__(self, "husband", spouse)


def create_person_list(
    people_data: List[Dict[str, Union[str, int]]]
) -> List[Person]:
    Person.people.clear()
    person_objects = [
        Person(person["name"], person["age"]) for person in people_data
    ]
    for person_obj, person in zip(person_objects, people_data):
        person_obj.set_spouse(
            wife_name=person.get("wife"),
            husband_name=person.get("husband"),
        )
    return person_objects
