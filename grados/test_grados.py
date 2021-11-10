import pytest
import grados

def test_conversion():
    assert grados.grados_fahrenheit(12) == 53.6
    assert grados.grados_fahrenheit(-4) == 24.8