# Asignacion por slicing
letras = ["a","b","c","d","e","f"]
letras[:3] = ['A','B',"F"]

print(letras)


# Lista paises 
paises = ["Colombia", "Mexico", "Argentina","Chile"]

print("Seleccionando pais usando index:",paises[0], paises[1])
print("Sleccionando rango de paises:",paises[1:])
print("Sleccionando rango de paises:",paises[-3:])


# Funciones de listas (Arrays)
# Del elimina la variable por completo
numeros = [0,1,2,3,4,5]

del(numeros) 
numeros = []
numeros[2:] = []

print(numeros)


##  Append - Agregar un valor al final del array
numeros2 = [1,2,3,5,]

numeros2.append(5)

print("Using append",numeros2)

## Pop - Elimina un valor del final del array 
numeros2.pop()

print("Using pop:",numeros2)

## Insert = Agregar un valor al principio del array 
numeros2.insert(0,0)

print("Using insert", numeros2)

#Extend - Agregar multiple valores al final del array
numeros2.extend([6,7,8,9])

print("Using extend:", numeros2 )

# Count
# Count: Conta numero de ocurrencias
numeros3 = [0,1,0,2,1,2,0,1,0,2,1,0]

print("Contanto cuantas veces se repite 1 usando count",numeros3.count(1))

#Index
print(numeros3.index(0))

index_1 = numeros3.index(1) # -> 1
print("Contando cuantas veces se repite 1 en la lista",numeros3.index(1,index_1+1))

