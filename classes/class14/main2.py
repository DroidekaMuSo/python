class Animal:
    adn = True

    def __init__(self, eyes: int, skin: str) -> None:
        self.eyes = eyes
        self.skin = skin

    def breath(self) -> 30:
        return """
        Quantity of breaths per minute
        :minute: int
        """

    def run(self) -> str:
        return """
        How it runs
        :return: str
        """

    def move(self):
        ...


class Cat(Animal):
    def __init__(self, color: str, race: str):
        super().__init__(2, "furry")

        self.color: color
        self.race: race


class Whale(Animal):
    def run(self) -> str:
        return "This animal does not run"

    def swim(self) -> str:
        return "Animal swims slow"


def run(x):
    return x.run()


print(run(Cat("red","black")))
print(Animal.__mro__)
print(Cat.__mro__)
