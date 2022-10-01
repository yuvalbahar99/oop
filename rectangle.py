# ------------------- IMPORTS -------------------
from shape import Shape

# -------------------FUNCTIONS -------------------


class Rectangle(Shape):

    def __init__(self, color, width, length):
        """
        the constructor of the class
        :param color: the color of the rectangle
        :param width: first rib of the rectangle
        :param length: second rib of the rectangle
        """
        super().__init__(color)
        self.width = width
        self.length = length

    def get_s(self):
        """
        ---
        :return: the area of the rectangle
        """
        return self.width * self.length

    def get_p(self):
        """
        ---
        :return: the perimeter of the rectangle
        """
        return 2 * (self.width + self.length)

    def set_width(self, width):
        """
        sets the value of the width
        :param width: first rib of the rectangle
        :return: None
        """
        self.width = width

    def set_length(self, length):
        """
        sets the value of the length
        :param length: second rib of the rectangle
        :return: None
        """
        self.length = length

    def get_width(self):
        """
        ---
        :return: the width of the rectangle
        """
        return self.width

    def get_length(self):
        """
        ---
        :return: the length of the rectangle
        """
        return self.length

    def add_rec(self, rectangle):
        """
        create a new rectangle- the area and perimeter are the sums of self and another rectangle
        :param rectangle: another rectangle (accept from self)
        :return: new rectangle- the connection of the both
        """
        # if type(rectangle) == "<class 'main.Rectangle'>" or type(rectangle) == "<class '__main.Square'>":
        if isinstance(rectangle, Rectangle):
            if self.color == rectangle.color:
                if self.width == rectangle.width or self.length == rectangle.width:
                    return Rectangle(self.color, self.width, self.length + rectangle.get_length())
                elif self.length == rectangle.width or self.width == rectangle.length:
                    return Rectangle(self.color, self.width + rectangle.get_width(), self.width)
        return None


if __name__ == 'rectangle':
    rec = Rectangle('red', 4, 5)
    assert rec.get_color() == 'red'
    assert rec.get_width() == 4
    assert rec.get_length() == 5
    assert rec.get_s() == 20
    assert rec.get_p() == 18
    rec.set_color('pink')
    rec.set_width(2)
    rec.set_length(6)
    assert rec.get_color() == 'pink'
    assert rec.get_width() == 2
    assert rec.get_length() == 6
    assert rec.get_s() == 12
    assert rec.get_p() == 16
    new_rec = rec.add_rec(Rectangle('pink', 2, 1))
    assert new_rec.get_color() == 'pink'
    assert new_rec.get_width() == 2
    assert new_rec.get_length() == 7
    assert rec.add_rec(Rectangle('red', 2, 6)) is None
    assert rec.add_rec(Rectangle('red', 3, 4)) is None