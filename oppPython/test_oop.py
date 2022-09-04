from oop import Point


def test_point():
    assert Point(3, 7).distance_to(Point(6, 11)) == 5.0


