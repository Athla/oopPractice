class Person:
    numberOfPeople = 0

    def __init__(self, name):
        self.name = name
        Person.addPerson()

    @classmethod
    def numberOfPeople_(cls):
        return cls.numberOfPeople

    @classmethod
    def addPerson (cls):
        cls.numberOfPeople += 1

p1 = Person("Jolyne")
p2 = Person("Jolene")
print(Person.numberOfPeople_())