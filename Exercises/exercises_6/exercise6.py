
while True:
    try:
        age = int(input("Type your age"))
        break
    except ValueError:
        print("It must be a number")

if age >= 18:
    print("You're an adult")

else:
    print("You're young")


