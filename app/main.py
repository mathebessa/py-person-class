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
        if wife_name:
            if wife_name in Person.people:
                self.wife = Person.people[wife_name]
        if husband_name:
            if husband_name in Person.people:
                self.husband = Person.people[husband_name]


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


people_data = [
    {"name": "Joey", "age": 30},
    {"name": "Rachel", "age": 28, "husband": "Ross"},
    {"name": "Ross", "age": 30, "wife": "Rachel"}
]

people = create_person_list(people_data)

joey = next(p for p in people if p.name == "Joey")

try:
    print(joey.wife)
except AttributeError:
    print("AttributeError levantado corretamente para Joey.wife")
