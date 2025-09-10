class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(
    people_data: list[dict[str, str | int | None]]
) -> list[Person]:
    persons = [Person(person["name"], person["age"])
               for person in people_data]

    for person_dict in people_data:
        person_instance = Person.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        if wife_name:
            person_instance.wife = Person.people[wife_name]
        if husband_name:
            person_instance.husband = Person.people[husband_name]
    return persons
