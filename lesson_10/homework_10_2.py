from abc import ABC, abstractmethod
from math import pi as pi


class Figure(ABC):
    @abstractmethod
    def get_figure_area(self):
        pass

    @abstractmethod
    def get_figure_perimeter(self):
        pass


class Square(Figure):
    def __init__(self, __length):
        self.__length = __length

    def get_figure_area(self):
        return self.__length ** 2

    def get_figure_perimeter(self):
        return self.__length * 4


class Rectangle(Figure):
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def get_figure_area(self):
        return self.__length * self.__width

    def get_figure_perimeter(self):
        return 2 * (self.__length + self.__width)


class Circle(Figure):
    def __init__(self, __radius):
        self.__radius = __radius

    def get_figure_area(self):
        return (self.__radius ** 2) * pi

    def get_figure_perimeter(self):
        return 2 * pi * self.__radius


def square_call():
    figures = [
        Square(5),
        Rectangle(4, 6),
        Circle(10)
        ]

    for x in figures:
        print(f"Figure`s area={x.get_figure_area()}, "
              f"Figure`s Perimeter={x.get_figure_perimeter()}")

def main():
    square_call()

if __name__ == "__main__":
    main()