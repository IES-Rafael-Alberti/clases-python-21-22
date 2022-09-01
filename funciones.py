def doble(numero):
    '''Duplica el número que recibe si es positivo
    '''
    if numero <= 0:
        return 0
    return numero * 2

def cuadruple(numero):
    return doble(doble(numero))

if __name__ == "__main__":
    pass