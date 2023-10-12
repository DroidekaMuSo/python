def divide(a: int, b: int):
    try:
        div = a/b
        return div
    except ZeroDivisionError as err:
        return f"Cannot divide using 0, \n {err}"


num1 = 5
num2 = 0
print(divide(num1, num2))
