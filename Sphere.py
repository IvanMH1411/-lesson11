from math import pi


class Sphere:
    radius = 1
    x = 0
    y = 0
    z = 0

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def get_volume(self):
        return pi * 4 * self.radius ** 3

    def get_radius(self):
        return self.radius

    def get_square(self):
        return 4 * pi * self.radius ** 2

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.radius ** 2 < (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2)