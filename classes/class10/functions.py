def add(num1: int, num2: int) -> int:
    total = num1 + num2

    return total


def res(num1: int, num2: int) -> int:
    total = num1 - num2

    return total


def res_default(num1: int, num2: int = 0) -> int:
    total = num1 - num2

    return total


# print(f"EL total de la suma es {add(num1=2, num2=5)}")
# print(f"EL total de la suma es {res(num1=2,num2=5)}")

def modify(value):
    value *= 2
    return value


# value_start = {"Luis", "Carlos"}
# value_modified = modify(value_start)
# print(value_modified)


def double(numbs: []) -> []:
    for i, n in enumerate(numbs):
        numbs[i] *= 2


lis_numbs = [10, 50, 100]


# double(lis_numbs)
# print(lis_numbs)

# print(id(lis_numbs))


def add_args(*args) -> int:
    total = 0

    for arg in args:
        total += arg

    return total


def add_args_k(**kwargs) -> int:
    total = 0

    for key, num in kwargs.items():
        print(f"adding the reference {key}")
        total += num

    return total


# print(f"Total is {add_args(2, 3, 4, 5, 6, 7, 8, 9)}")
# print(f"Total is {add_args_k(num1=1, num2=2, num3=3)}")


def factorial(number: int) -> int:
    if number == 1:
        return 1

    return number * factorial(number - 1)


def fibonacci(number: int) -> int:
    if number == 1 or number == 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


print(factorial(60))
print(fibonacci(60))
