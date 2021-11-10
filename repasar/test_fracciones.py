import pytest

from fraccion import Fraccion

def test_fracciones():
    f1 = Fraccion(3,4)
    f2 = Fraccion(5)
    assert str(f1) == "3/4"
    assert str(f2) == "5/1"
    f3 = f1 * f2
    assert str(f3) == "15/4"
 

