def calcula_datos(lista):
    suma = 0
    cantidad = 0
    for numero in lista:
        suma += numero
        cantidad += 1
    media = suma / cantidad
    return suma, cantidad, media

if __name__ == "__main__":
    print(calcula_datos([4,6,7,8,9]))
    lista = []
    while True:
        try:
            numero = int(input("Introduce un número (0 finalizar): "))
            if numero == 0:
                break
            lista.append(numero)
        except ValueError:
            print("Solo números")
    print(calcula_datos(lista))