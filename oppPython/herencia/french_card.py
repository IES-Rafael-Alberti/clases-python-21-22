from herencia.card import Card


class FrenchCard(Card):
    FIGURAS = ("JACK", "QUEEN", "KING")
    PALOS = ("SPADE", "HEART", "TREBOL", "DIAMOND")

    def __init__(self, palo, valor=None):
        if palo.upper() == "JOKER":
            self.palo = palo
            self.valor = 0
        else:
            super().__init__(palo, valor)
