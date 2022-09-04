class Fraction:
    def __init__(self, numerador: int, denominador: int = 1):
        if not isinstance(numerador, int) or not isinstance(denominador, int):
            raise ValueError("Usage: Fraction(int[, int])")
        my_mcd = self.mcd(numerador, denominador)
        self.numerador = numerador // my_mcd
        self.denominador = denominador // my_mcd

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise ValueError("Only operations between Fraction")
        return Fraction(self.numerador * other.denominador + self.denominador * self.numerador, self.denominador * other.denominador)

    def __eq__(self, other):
        return self.numerador == other.numerador and self.denominador == other.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __pow__(self, power, modulo=None):
        pf = float(power)
        return Fraction(int(self.numerador ** pf), int(self.denominador ** pf))

    def __float__(self):
        return self.numerador / self.denominador

    def mcd(self, m: int, n: int) -> int:
        if m % n == 0:
            return n
        else:
            return self.mcd(n, m % n)


if __name__ == '__main__':
    f1 = Fraction(2, 3)
    f2 = f1 + 4
    print(f1)