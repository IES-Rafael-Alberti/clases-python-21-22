class Fraccion:
    '''Define una fracción.

Están definidos los métodos para TODAS las operaciones aritméticas.
'''
    def __init__(self, numerador, denominador=1):
        self.numerador = numerador
        self.denominador = denominador
        print("Ya me he construido")

    def __str__(self):
        print("Me van a convertir a String")
        return f"{self.numerador}/{self.denominador}"

    def __mul__(self, otro):
        return Fraccion(self.numerador*otro.numerador, self.denominador*otro.denominador)


if __name__ == "__main__":
    f1 = Fraccion(5)
    print(f1)
    f2 = Fraccion(6,5)
    print(f2)
    f3 = f1 * f2
    print(f3)
    print(Fraccion.__doc__)