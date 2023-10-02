name = input("What is your name?")
age = input("How old are you?")
address = input("What is your address?")

user = {
    "name": name,
    "age": age,
    "address": address
}

print(f"{name} is {age} years old and lives in {address}")
print(user)