def datos_lista(lista):
    cantidad = 0
    suma = 0
    for numero in lista:
        suma += numero
        cantidad += 1
    
    return suma, cantidad, suma/cantidad

if __name__ == "__main__":
    sumita, longitud, medita = datos_lista([3, 7, 5, 8])
    print(f"La suma es {sumita} y la media {medita}, de la lista con {longitud} elementos")