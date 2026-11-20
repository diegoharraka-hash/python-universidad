import copy

original = {"nombre": "Ana", "intereses": ["cine", "futbol"]}

copia = copy.deepcopy(original)

copia["intereses"].append("musica")

print("original:", original["intereses"])
print("copia:", copia["intereses"])