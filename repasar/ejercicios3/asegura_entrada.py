# Opción 1
def asegura_int(texto):
    while True:
        try:
            valor = int(input(texto))
            break
        except ValueError:
            print("No es un número")
    return valor

def asegura_float(texto):
    while True:
        try:
            valor = float(input(texto))
            break
        except ValueError:
            print("No es un número")
    return valor

# Opción 2
#### Abstenerse noobs
def tipo_int(texto):
    return int(texto)

def tipo_float(texto):
    return float(texto)

#def asegura_numero(texto, funcion_tipo = lambda texto_entrada : int(texto_entrada)):
def asegura_numero(texto, funcion_tipo = int):
    while True:
        try:
            valor = funcion_tipo(input(texto))
            break
        except ValueError:
            print("No es un número")
    return valor
