# ------------------- IMPORTS -------------------
from container import Container

# -------------------FUNCTIONS -------------------


def main():
    """
    Checks the functions of all the classes
    :return: None
    """
    my_container = Container()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    main()