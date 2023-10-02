number = int(input("Insert a number between 0 & 9"))

while number > 0 and number < 9:
    number = int(input("Insert a number between 0 & 9"))

    if number in range(9):
        print("Number in range")
