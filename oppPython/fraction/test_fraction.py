from fraction.fraction import Fraction


def test_fraction():
    f1 = Fraction(2/3)
    f2 = Fraction(2, 3)
    f3 = f1 + f2
    assert f3 == Fraction(4, 3)
    f1 = Fraction(7, 3)
    f2 = Fraction(1, 2)
    f3 = f1 ** f2
    assert f3 == Fraction(2)
