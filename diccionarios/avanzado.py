# Sintaxis avanzada de listas y diccionarios

#lista = list()
#while True:
#    try:
#        numero = input("Dame un numero")
#        if numero == "fin":
#            break
#        lista.append(int(numero))
#    except ValueError:
#        print("Solo números...")

#Formato tradicional
#lista2 = list()
#for numero in lista:
#    if numero % 2 == 0:
#        lista2.append(numero)

#Listas por comprensión
#lista2 = [ numero for numero in lista if numero % 2 == 0 ]
#print(*lista2)

#Empaquetado y desempaquetado
lista_a = [ "Ana", "Valeria", "Carmen", "José", "Fernando" ]
lista_b = [ 12, 10, 14, 4, 15 ]
#lista_final = zip(lista_a, lista_b)
lista_final = [ {"nombre": nombre, "edad": edad} for nombre, edad in zip(lista_a, lista_b) ]

print(*lista_final, sep="\n")


