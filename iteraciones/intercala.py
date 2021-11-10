lista = ["Ana", "Fernanda", "Luisa", "Mercedes"]
lista2 = [ "Gonzalo", "Javi", "Hugo", "Cancelo" ]

longitud = max(len(lista), len(lista2))

intercaladas = []
for i in range(longitud):
    if i<len(lista):
        intercaladas.append(lista[i])
    if i<len(lista2):
        intercaladas.append(lista2[i])

print(intercaladas)

parejas = zip(lista, lista2)
intercaladas = []
for pareja in parejas:
    for elemento in pareja:
        intercaladas.append(elemento)

print(intercaladas)
