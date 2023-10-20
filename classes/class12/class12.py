class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self, phrase):
        print(f"This {self.name} is saying: {phrase}")


person1 = Person("Juan", 25)

print(person1.name)
print(person1.name)
