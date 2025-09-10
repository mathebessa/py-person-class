class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(
    people_data: list[dict[str, str | int | None]]
) -> list[Person]:
    persons = [Person(p["name"], p["age"]) for p in people_data]

    for p in people_data:
        person = Person.people[p["name"]]
        wife = p.get("wife")
        husband = p.get("husband")
        if wife:
            person.wife = Person.people[wife]
        if husband:
            person.husband = Person.people[husband]
    return persons
