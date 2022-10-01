# ------------------- IMPORTS -------------------
from rectangle import Rectangle

# -------------------FUNCTIONS -------------------


class Square(Rectangle):

    def __init__(self, color, width):
        """
        the constructor of the class
        :param color: the color of the square
        :param width: the rib of the square
        """
        super().__init__(color, width, width)

    def set_width(self, width):
        """
        sets the value of the width
        :param width: the rib of the square
        :return: None
        """
        self.width = width
        self.length = width

    def set_length(self, length):
        """
        sets the value of the width
        :param length: the rib of the square
        :return: None
        """
        self.width = length
        self.length = length

    def get_width(self):
        """
        ---
        :return: the rib of the square
        """
        return self.width

    def get_length(self):
        """
        ---
        :return: the rib of the square
        """
        return self.width


if __name__ == 'square':
    square = Square('red', 2)
    assert square.get_color() == 'red'
    assert square.get_width() == 2
    assert square.get_length() == 2
    assert square.get_s() == 4
    assert square.get_p() == 8
    square.set_color('blue')
    square.set_width(6)
    assert square.get_color() == 'blue'
    assert square.get_width() == 6
    assert square.get_length() == 6
    assert square.get_s() == 36
    assert square.get_p() == 24
    square.set_length(1)
    assert square.get_width() == 1
    assert square.get_length() == 1
    assert square.get_s() == 1
    assert square.get_p() == 4