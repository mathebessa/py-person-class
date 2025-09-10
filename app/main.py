class Person:
    people = {}

    def __init__(
        self,
        name: str,
        wife_name: str = None,
        husband_name: str = None,
    ) -> None:
        self.name = name
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
        return f"Person(name={self.name})"


def create_person_list(names: list) -> list:
    return [Person(name) for name in names]
