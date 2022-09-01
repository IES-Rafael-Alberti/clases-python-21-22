import pytest
from digitos_binario import digitos_binario_budda as digitos_binario, digitos_binario_de_gonzalo

def test_digitos_binario():
    assert digitos_binario(47) == 6
    assert digitos_binario(127) == 7
    assert digitos_binario(15) == 4
    assert digitos_binario(16) == 5
    assert digitos_binario(0) == 1



def test_digitos_de_gonzalo():
    assert digitos_binario_de_gonzalo(47) == 6
    assert digitos_binario_de_gonzalo(127) == 7
    assert digitos_binario_de_gonzalo(15) == 4
    assert digitos_binario_de_gonzalo(16) == 5
    assert digitos_binario_de_gonzalo(0) == 1

def test_aprobados():
    assert aprobado("Bartus") == False

