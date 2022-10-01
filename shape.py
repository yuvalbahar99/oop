# -------------------FUNCTIONS -------------------
class Shape:

    def __init__(self, color):
        """
        the constructor of the class
        :param color: the color of the shape
        """
        self.color = color

    def set_color(self, color):
        """
        the function receives a new color and sets it to the shape
        :param color: the new color of the shape
        :return: None
        """
        self.color = color

    def get_color(self):
        """
        ---
        :return: the color of the shape
        """
        return self.color

    def get_s(self):
        """
        the function will be in each shape type
        :return: None
        """
        pass

    def get_p(self):
        """
        the function will be in each shape type
        :return: None
        """
        pass


if __name__ == 'shape':
    shape = Shape('red')
    assert shape.get_color() == 'red'
    shape.set_color('green')
    assert shape.get_color() == 'green'
    assert shape.get_s() is None
    assert shape.get_p() is None
