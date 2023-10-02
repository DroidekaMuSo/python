lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

lista = list(set(lista))

lista.sort(reverse=True)

for element in lista:
    if element % 2 == 1:
        lista.remove(element)

addittion = sum(lista)

lista.insert(0, addittion)

print(lista)
