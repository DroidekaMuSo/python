number1 = int(input("Insert number 1"))
number2 = int(input("Insert number 2"))
option = int(input(f"""Insert an option 
                   1) +
                   2) -
                   3) *
                   4) Escape
                   """))

if(option > 0):
    if (option == 1):
        result = number1 + number2
        print(f"Result: {result}")
    elif (option == 2):
        result = number1 - number2
        print(f"Result: {result}")
    elif (option == 3):
        result = number1 * number2
        print(f"Result: {result}")
    elif (option == 4):
        print("Bye")
    else:
        print("Option not valid") 
else:
    print("Option not valid")


