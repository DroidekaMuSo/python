class Person:
    def __init__(self, name: str, last_name: str, birth_year: str):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def __str__(self):
        return f"""
        Name: {self.name}
        Last name: {self.last_name}
        Year of birth: {self.birth_year}
        """


class Client(Person):
    def __init__(self, name: str, last_name: str, birth_year: str,nickname: str, email: str, password: str, premium: bool, address: str, cart: tuple = ()):
        super().__init__(name, last_name, birth_year)

        self.nickname = nickname
        self.email = email
        self._password = password
        self.premium = premium
        self._address = address
        self._cart = cart

    def add_product(self, product_id):
        ...

    def delete_product(self, product_id):
        ...

    def checkout(self):
        ...

    def update_cart(self):
        ...

    def __str__(self):
        return f"""
        Name: {self.name}
        Last name: {self.last_name}
        Nickname: {self.nickname}
        Email: {self.email}
        Premium: {self.premium}
        """


client1 = Client("Diego", "Munoz", "1998", "Droideka", "diego.munoz_solis@hotmail.com", "12345abcde", False, "Street 1")
print(client1.__str__())