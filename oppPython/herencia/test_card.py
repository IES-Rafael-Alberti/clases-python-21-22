from herencia.card import Card
from herencia.french_card import FrenchCard
import pytest

def test_card():
    miCarta = Card("ORO", 3)
    miCarta = Card("ORO", "rey")
    miCarta = Card("ORO", "caballo")

    with pytest.raises(ValueError, match=r".* palo:.*"):
        miCarta = Card("OROS", 3)
    with pytest.raises(ValueError, match=r".* valor:.*"):
        miCarta = Card("ORO", 0)
        miCarta = Card("ORO", 12)
        miCarta = Card("ORO", "lupita")

    miCarta = Card("COPA", "sota")
    miCarte = FrenchCard("JOKER")
    miCarte = FrenchCard("DIAMOND", 5)
    assert True
