colores = set({"Rojo","Blanco","Azul"})

colores.update({"Violeta", "Dorado"})

if("Celeste" in colores):
    colores.remove("Celeste")
else:
    colores.discard("Celeste")

colores.remove("Blanco")
colores.remove("Dorado")


print(colores)