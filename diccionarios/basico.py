# Declarar diccionario con contenido
# clave = dato por el que accedo a los valores
# valor = dato almacenado
diccionario = { 
                "clave1" : "valor1",
                "clave2" : "valor2",
                "clave3" : "valor3",
                "clave4" : "valor4",
                "clave5" : "valor5",
                "clave6" : "valor6",
              }

# Declarar diccionario vacío
# v1
diccionario_vacio1 = {}
# v2
diccionario_vacio2 = dict()

# Con listas también funciona...
lista_vacia1 = []
lista_vacia2 = list()

# Introducir valores en el diccionario
# Si la clave es nueva, se crea un nuevo elemento
diccionario["clave7"] = "valor7"
# Si la clave existe, se modifica el valor almacenado
diccionario["clave6"] = "valor62"

# Para acceder a los valores
print(diccionario["clave3"])
# Cuidado, en este caso si la clave no existe se produce un error!!!
try:
    print(diccionario["clavea4"])
except KeyError:
    print("Como os decía, da error")

# Recorridos
claves = list(diccionario.keys())
valores = diccionario.values()
diccionario_en_tuplas = list(diccionario.items())
print(*diccionario_en_tuplas)

# Recorrido completo
for clave, valor in diccionario.items():
    print(f"El valor con la clave {clave} es {valor}")

# Comprobación de que existe una clave determinada
mi_clave = input("Dime una clave del diccionario: ")
if mi_clave in diccionario.keys():
    print(f"Su valor es {diccionario[mi_clave]}")
else:
    print("Te has equivocado, esa clave no está en el diccionario")
    
# Recorrer sólo las claves
for clave in diccionario.keys():
    print(f"Clave: {clave}")
    
# Recorrer sólo los valores
for valor in diccionario.values():
    print(f"Valor: {valor}")

# Contenido actualizado
print("Esto es lo nuevo")

