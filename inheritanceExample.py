#inheritance example
#upper level class/generalization class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I'm {self.name} with {self.age} years old")
#multiple classes that are similar
class Cat(Pet):    
    def speak(self):
        print ("meow")
class Dog(Pet):
    def speak(self):
        print ("bark")

p = Pet("Dong", 18)
p.show()
c = Cat("Bronkl", 16)
c.show()