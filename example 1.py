#OOP IN PYTHON

class Dog:
    #special methods
    def __init__(self, name):
        #atribute of class dog
        self.name = name
        print(name)
    #methods are functions that go inside of a class
    def getName(self):
        return self.name
d = Dog("Tim")
