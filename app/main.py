class Pessoa:
    people: dict[str, "Pessoa"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Pessoa.people[name] = self


def create_person_list(
    people_data: list[dict[str, str | int | None]]
) -> list[Pessoa]:
    persons = [Pessoa(person["name"], person["age"])
               for person in people_data]

    for person_dict in people_data:
        person_instance = Pessoa.people[person_dict["name"]]
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        if wife_name:
            person_instance.wife = Pessoa.people[wife_name]
        if husband_name:
            person_instance.husband = Pessoa.people[husband_name]
    return persons
