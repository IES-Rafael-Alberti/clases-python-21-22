import pytest

from rectangulos import Rectangulo
from puntos import Punto

def test_areadelrectangulo():
    with pytest.raises(ValueError):
        Punto("3",4)
        
    p1 = Punto(3,4)
    p2 = 5
    with pytest.raises(ValueError):
        Rectangulo(p1,p2)
    p2 = Punto(7,8)
    mirectangulo = Rectangulo(p1,p2)
    assert mirectangulo.area() == 16

