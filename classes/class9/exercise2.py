def welcome(city):
    return f"Hi, welcome to {city}"


welcome("Mexico")


def average(lista: list):
    length = len(lista)
    add = sum(lista)

    total = add/length

    return total


print(average([1, 2, 3, 4, 5]))


def is_odd(num1: int,num2: int):
    if num1 % num2 == 0:
        return f"{num1} is divisible by {num2}"
    elif num2 % num1 == 0:
        return f"{num2} is divisible by {num1}"
    else:
        return f"The are not divisible between them"


print(is_odd(3, 2))
