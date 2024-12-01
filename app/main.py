class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_people = []
    for person in people:
        new = Person(person["name"], person["age"])
        new_people.append(new)

    new_people[0].wife = new_people[5]
    new_people[5].husband = new_people[0]

    new_people[3].wife = new_people[4]
    new_people[4].husband = new_people[3]

    return new_people
