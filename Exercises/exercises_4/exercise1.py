dicts = {
    "paises": {"England", "USA", "Mexico"}
}


dicts["paises"].update({"Island", "Italy", "Argentina", "Portugal", "USA"})

dicts["paises"].discard("Chile")
dicts["paises"].remove("Italy")

print(dicts)
