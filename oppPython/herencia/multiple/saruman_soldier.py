from herencia.multiple.enemy import Enemy
from herencia.multiple.orc import Orc


class SarumanSoldier(Enemy, Orc):
    def __init__(self, live_points, level, tribe):
        Enemy.__init__(self, live_points, level)
        Orc.__init__(self, tribe)
