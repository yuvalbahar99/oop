# ------------------- IMPORTS -------------------
import math
from shape import Shape

# -------------------FUNCTIONS -------------------


class Circle(Shape):

    def __init__(self, color, r):
        """
        the constructor of the class
        :param color: color of the circle
        :param r: radius of the circle
        """
        super().__init__(color)
        self.r = r

    def get_s(self):
        """
        ---
        :return: the surface of the circle
        """
        return (self.r ** 2) * math.pi

    def get_p(self):
        """
        ---
        :return: the perimeter of the circle
        """
        return 2 * self.r * math.pi

    def get_r(self):
        """
        ---
        :return: the radius of the circle
        """
        return self.r

    def set_r(self, r):
        """
        sets the value of the radius
        :param r: the radius of the circle
        :return: None
        """
        self.r = r


if __name__ == 'circle':
    circle = Circle('red', 3)
    assert circle.get_color() == 'red'
    assert circle.get_r() == 3
    assert circle.get_s() == 9 * math.pi
    assert circle.get_p() == 6 * math.pi
    circle.set_color('brown')
    circle.set_r(2)
    assert circle.get_color() == 'brown'
    assert circle.get_r() == 2
    assert circle.get_s() == 4 * math.pi
    assert circle.get_p() == 4 * math.pi
