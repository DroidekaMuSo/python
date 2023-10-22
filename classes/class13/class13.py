class Dog:
    # Attributes of the class
    specie = "Mammal"

    #     Constructor
    def __init__(self, name: str, race: str):
        # Attributes of instance
        self.name = name
        self.race = race

    def __str__(self):
        return f"Name: {self.name}, Race: {self.race}, specie: {self.specie}"

    @staticmethod
    def bark(self):
        print("Wow")

    @staticmethod
    def walk(steps):
        print(f"Walking {steps} steps")


class Person:
    def __init__(self,name, last_name, dog):
        self.name = name
        self.last_name = last_name
        self.dog = dog

    def __str__(self):
        return f"My name is {self.name} {self.last_name} and my dog's name is {self.dog.__str__()}"


dog1 = Dog("Bruno", "Variant")
person1 = Person("Diego", "Munoz", dog1)


print(F"Its name is {dog1.name}")
print(F"Its race is {dog1.race}")
print(F"It's a {dog1.specie}")
print("-------------------------")
print(F"{dog1.bark(None)}")
print(F"{dog1.walk(100)}")

print(person1)

