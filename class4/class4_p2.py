# Exercise 1
year = 1998

if year:
    if year >= 1920 and year <= 1940:
        print("You ar from the silent geneartion")
    elif year >= 1946 and year <= 1964:
        print("You are from the baby boomer generation")
    elif year >= 1965 and year <= 1979:
        print("You are from the X generation")
    elif year >= 1980 and year <= 2000:
        print("You are from the Y generation")
    elif year >= 2001 and year <= 2010:
        print("You are from the Z generation")
    else:
        print("Unknow generation")
else:
    print("Must be a number")


# Exercise 2
age = 15
longevity = 10
incomes = 1500

if age >= 18 and ((longevity >= 3 and incomes >= 2500) or incomes >= 4000):
    print("Credit approved")
else:
    print("Credit not approved")


#Exercise 3
name = input("What is your name?")
group = input("What do you rather?")

