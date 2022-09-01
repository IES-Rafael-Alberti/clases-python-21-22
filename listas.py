# lista = [ 3, 5, 7, 9, 2 ]
# lista_texto = [ 'Hola', 'Hello', 'Hi', 'Ciao' ]

# for elemento in lista:
#     print(elemento)

# for i in range(len(lista_texto)):
#     print(i, lista_texto[i])

# for i, elemento in enumerate(lista_texto):
#     print(i, elemento)

# for elemento in enumerate(lista_texto):
#     print(elemento)

# lista_ordenada = sorted(lista_texto)
# lista_texto.sort()

# if "Hola" in lista_texto:
#     print("Si está")

# cadena = " ".join(lista_texto)
# print(cadena)

a = [ 3, 6, 1]
b = a

if b == a:
    print("Tienen el mismo contenido")

if b is a:
    print("Son alias")

a = [ 3, 6, 1]
b = a[:]

if b == a:
    print("Tienen el mismo contenido")

if b is a:
    print("Son alias")

b[1] = 7
print(a)
print(b)