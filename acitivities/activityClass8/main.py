def leap_year(year):
    if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
        return True


year = int(input("Insert the year"))


if year > 0:
    check = leap_year(year)

    if check:
        print(f"The year {year} is leap")
    else:
        print(f"The year {year} is not leap")
else:
    print(f"The year is invalid {year}")




