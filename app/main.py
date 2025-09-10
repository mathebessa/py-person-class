class Person:
    people = {}

    def __init__(self, name: str, wife_name: str = None, husband_name: str = None) -> None:
        self.name = name
        Person.people[name] = self

        if wife_name is not None:
            self.wife = Person.people[wife_name]
        if husband_name is not None:
            self.husband = Person.people[husband_name]


person1 = Person("John", wife_name="Jane")
person2 = Person("Jane", husband_name="John")
person3 = Person("Alice")

print(person1.name)
print(person1.wife.name)
print(person2.name)
print(person2.husband.name)

try:
    print(person3.wife)
except AttributeError as e:
    print("AttributeError:", e)
