def elimina_primero(lista):
    del lista[0]
    return lista

def borra(g):
    g = 0

palabras = [ "pepe", "luis", "gota", "jose", "javier", "es", "bueeeno" ]

b = elimina_primero(palabras)
del b[0]
print(palabras)

texto = 7777
borra(texto)
print(texto)