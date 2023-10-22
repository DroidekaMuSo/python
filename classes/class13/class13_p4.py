class Person:
    type = "Human"
    __salary = 2000

    def __init__(self, name, last_name):
        self.name = name
        self._last_name = last_name

    @staticmethod
    def __happy():
        print("Don't care")

    def age(self):
        return 31


person1 = Person("Nick", "Perez")

print(f"Result1: {person1.type}")
# print(f"Result2: {person1.__salary}")
print(f"Result3: {person1.name}")
# print(f"Result4: {person1.__last_name}")
# print(f"Result5: {person1.__happy()}")
print(f"Result6: {person1.age()}")

