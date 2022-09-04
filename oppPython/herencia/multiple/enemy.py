class Enemy:
    def __init__(self, live_points, level):
        self.live_points = live_points
        self.level = level

    def attack(self):
        return f"{self.level} Attack!!!!!"
