# While
# Exercise 1
number = int(input("Please, insert a number: "))

while number != 0:
    number = int(input("Insert a number again"))

# Exercise 2
numbers = [1, 2, 3, 4, 5]

while numbers:
    print(numbers.pop())

print("Thanks for using our service")

# While else / Rarely used
numbers = [1, 2, 3, 4, 5]

while numbers:
    print(numbers.pop())
    
print("Thanks for using our service")

# Break -> Breaks the flow
# Continue -> Skip the actions that are in the look after the continue
# Pass -> Nada

while number != 100:

    if number == 5:
        continue

    if number == 50:
        break

    number += 1
    print(number)
    break

# For loop

letters = ["a", "b", "c", "d", "e"]
print("For loop")
for letter in letters:
    print(letter)


# Range
things = range(1, 10, 2)
print(things)
