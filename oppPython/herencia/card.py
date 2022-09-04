class Card:
    LIMITE = 10
    FIGURAS = ("SOTA", "CABALLO", "REY")
    PALOS = ("ORO", "BASTO", "COPA", "ESPADA")

    def __init__(self, palo, valor):
        if not palo.upper() in self.PALOS:
            raise ValueError(f"El palo: {palo}, no es válido")
        if isinstance(valor, int):
            if valor < 1 or valor > self.LIMITE:
                raise ValueError(f"El valor: {valor}, no es válido")
        elif isinstance(valor, str):
            if not valor.upper() in self.FIGURAS:
                raise ValueError(f"El valor: {valor}, no es válido")
        else:
            raise ValueError(f"El valor: {valor}, no es válido")
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}s"