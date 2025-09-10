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

        if wife_name is not None:
            if wife_name not in Person.people:
                raise ValueError(
                    f"The person {wife_name} has not been registered."
                )
            self.wife = Person.people[wife_name]

        if husband_name is not None:
            if husband_name not in Person.people:
                raise ValueError(
                    f"The person {husband_name} has not been registered."
                )
            self.husband = Person.people[husband_name]

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people_data: list) -> list:
    for person_data in people_data:
        name = person_data["name"]
        age = person_data["age"]
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        Person(name, age, wife_name, husband_name)
    return list(Person.people.values())
