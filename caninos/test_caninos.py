import pytest
import agnos_caninos

def test_caninos1():
    assert agnos_caninos.agnos_caninos(1) == 10.5
    assert agnos_caninos.agnos_caninos(2) == 21
    assert agnos_caninos.agnos_caninos(5) == 33