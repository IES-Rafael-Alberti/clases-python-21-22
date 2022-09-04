import math
from datetime import datetime


class Point:
    class_attribute = 6

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y} - {self.class_attribute})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def distance_to(self, **kargs):
        kargs.get('p1')
        distances = [math.sqrt((self.x - point.x) ** 2 +
                     (self.y - point.y) ** 2)
                     for point_name, point in kargs.items()]
        return sum(distances)


if __name__ == '__main__':
    point1 = Point(3, 7)
    # class attributes must be used only with class name reference
    # avoid if possible referencing through instances
    # if it is necessary, remember that assigning new values using instance reference
    # will make that attribute an instance attribute, forgetting the class attribute
    point2 = point1
    point3 = point1 + point2
    point4 = point3 - point1
    point4 += point3
    print(point1)
    print(point2)
    print(point3)
    print(point4)




