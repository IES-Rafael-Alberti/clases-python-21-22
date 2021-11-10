from herencia import *
import pytest

def test_herencia():
    ha=HijoA()
    hb = HijoB()

    assert ha.atributo1=="HijoA"
    assert hb.atributo1=="HijoB"