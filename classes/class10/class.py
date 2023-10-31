# def divide(a: int, b: int):
#     if b == 0:
#         return "Cannot divide using 0"
#
#     return a/b
#
#
# print(divide(9, 0))

# "A2XhcPJPD9BuMKELKz12a1oMNNCZx"

try:
    num1 = int(input("Insert your calculators number"))
    num2 = int(input("Insert your second number"))

    print(num1 / num2)
except TypeError as err:
    print(err)
    print("Incorrect data")

