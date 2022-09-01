import math

def digitos_binario(numero):
    digitos = 1
    ## Aumento los dígitos mientras el número sea menor que 2 elevado a dígitos
    while 2**digitos <= numero:
        digitos += 1
    return digitos

def digitos_binario_de_gonzalo(numero):
    ## Usa una función de Python que pasa un número a binario
    en_binario = bin(numero)
    ## Pero esto añade al principio '0b' y eso hay que quitarlo...
    return len(en_binario[2:])

def digitos_binario_budda(numero):
    return int(math.log2(numero)) + 1 if numero else 1
