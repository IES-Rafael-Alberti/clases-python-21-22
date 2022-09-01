import pytest
from funciones import doble, cuadruple

def test_doble_negativo():
    assert doble(-4) == 0

def test_doble_positivo():
    assert doble(4) == 8

def test_cuadruple_negativo():
    assert cuadruple(-4) == 0

def test_cuadruple_positivo():
    assert cuadruple(8) == 32



