import pytest
from ejercicio3_1 import *

def test_discriminante_raiz_negativa():
    assert calcula_raices_2grado(1, 1, 1) is None, "Cálculo incorrecto del discriminante"

#def test_discriminante_0():
#    assert calcula_raices_2grado(1, 2, 1) == (-1, -1), "Cálculo incorrecto cuando el discriminante es cero"

#def test_raices_diferentes():
#    assert calcula_raices_2grado(2, 3, 1) == (-0.5, -1), "Cálculo incorrecto cuando el discriminante no es cero"

#def test_division_por_cero():
#    assert calcula_raices_2grado(0, 3, 1) is None, "Cálculo incorrecto cuando a es cero"
