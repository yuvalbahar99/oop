# ------------------- IMPORTS -------------------
from square import Square
from rectangle import Rectangle
from circle import Circle
import random

# -------------------CONSTANTS -------------------
COLORS = ['red', 'yellow', 'blue', 'green', 'orange', 'brown', 'pink', 'purple']
COLORS_DICT = {'red': 0,
               'yellow': 0,
               'blue': 0,
               'green': 0,
               'orange': 0,
               'brown': 0,
               'pink': 0,
               'purple': 0}

# -------------------FUNCTIONS -------------------


class Container:

    def __init__(self):
        """
        the constructor of the class
        """
        self.shapes_dict = {}
        self.dict_len = 0

    def generate(self, x):
        """
        the function creates X new shapes and adds them to the dictionary of the shapes
        :param x: the number of shapes that the function constructs
        :return: None
        """
        for i in range(0, x):
            color_num = random.randint(0, len(COLORS) - 1)
            color = COLORS[color_num]
            first_size = random.randint(1, 50)  # width or radius
            shape_num = random.randint(0, 2)
            if shape_num == 0:  # rectangle
                second_size = random.randint(1, 50)  # length
                self.shapes_dict[self.dict_len] = Rectangle(color, first_size, second_size)
            elif shape_num == 1:  # square
                self.shapes_dict[self.dict_len] = Square(color, first_size)
            else:  # circle
                self.shapes_dict[self.dict_len] = Circle(color, first_size)
            self.dict_len += 1

    def sum_areas(self):
        """
        calculates the total areas
        :return: the sum of all the areas of the shapes in the dictionary
        """
        sum_s = 0
        if self.dict_len == 0:
            return 0
        for i in self.shapes_dict.values():
            sum_s += i.get_s()
        return sum_s

    def sum_perimeters(self):
        """
        calculates the total perimeters
        :return: the sum of all the perimeters of the shapes in the dictionary
        """
        sum_p = 0
        if self.dict_len == 0:
            return 0
        for i in self.shapes_dict.values():
            sum_p += i.get_p()
        return sum_p

    def count_colors(self):
        """
        counts how many shapes are from each color- and updates in the colors dictionary
        :return: the colors dictionary
        """
        for i in self.shapes_dict.values():
            for j in COLORS_DICT.keys():
                if i.get_color() == j:
                    COLORS_DICT[j] += 1
        return COLORS_DICT


if __name__ == 'container':
    cont = Container()
    cont.generate(20)
    assert cont.sum_areas() > 0
    assert cont.sum_perimeters() > 0
    dictionary = cont.count_colors()
    counter = 0
    for a in dictionary.values():
        counter += a
    assert counter == 20
