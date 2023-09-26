dic_numbers = {0: 0, 1: 1, 2: 2}
person = {"name": ["Luis", "Mariana"], "lastName": "Gutierrez"}
list_num = [0, 1, 2]

# print(dic_numbers[0], list_num[0], person["name"][0])

winners = {
    1990: "Alemania",
    1994: "Brasil",
    1998: "Francia",
    2002: "Brasil",
    2006: "Italia",
    2010: "Espania",
    2014: "Alemania",
    2018: "Francia"
}

year = int(input("Year?"))

if (year in winners):
    print(winners[year])
else:
    print("A football mundial was not played in that year")
