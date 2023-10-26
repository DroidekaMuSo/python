class Cetacean:
    def __init__(self, notes: str, lives: str, weight: str):
        self.notes = notes
        self.lives = lives
        self.weight = weight

    def born(self):
        ...

    def swim(self):
        ...


class Mammal(Cetacean):
    def __init__(self, notes: str, lives: str, weight: str, cant_mamas: str, life_expectancy: str):
        super().__init__(notes, lives, weight)
        self.cant_mamas = cant_mamas
        self.life_expectancy = life_expectancy

    def __str__(self):
        return f""" 
        Notes: {self.notes}
        Lives: {self.lives}
        Weight: {self.weight}
        Camt_mamas: {self.cant_mamas}
        Life_expectancy: {self.life_expectancy}
        """

    def suck(self):
        ...

    def born(self):
        ...


class SeaAnimal(Cetacean):
    def __init__(self, notes: str, lives: str, weight: str, has_gils: bool, specie: str):
        super().__init__(notes, lives, weight)
        self.has_gills = has_gils
        self.specie = specie

    def __str__(self):
        return f"""
        Notes: {self.notes}
        Lives: {self.lives}
        Weight: {self.weight}
        Gills: {self.has_gills}
        Specie: {self.specie}
        """

    def swim(self):
        ...


cetacean1 = SeaAnimal("Cetaceo mas grande en peligro critico de extincion", "Bering Island", "30 - 55", False,"Vaquita Marina")
cetacean2 = Mammal("", "", "70 - 110", "2.4", "5 years")

print(cetacean1)
print("======================================================================")
print(cetacean2)
