# Complete the Shapes class group.
# Add a method called "getArea" to both Circle and Square classes.
# Return the values as necessary.
# Hint: pi (3.14) requires:from math import pi

import math


class Shape:

    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled


class Square(Shape):  # side * side

    def __init__(self, side):
        super().__init__()
        self.__side = side

    def get_side(self):
        return self.__side

    def get_area(self):
        return self.__side * 2

    def get_perimeter(self):
        return self.__side * 4


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return math.pi * self.__radius ** 2  # a straight line from the center to the circumference
        # of a circle or sphere. Radius is half of a circle.

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


side = Square(4)

print("Area of a square is:", format(side.get_area(), "0.2f"))  # two decimal.
print("Perimeter of a square is:", side.get_perimeter())
print(side.get_filled())
print(side.get_color())

c1 = Circle(20)

print("\nArea of a circle is:", format(c1.get_area(), "0.2f"))
print("Perimeter of a circle is:", format(c1.get_perimeter(), "0.2f"))
print(c1.get_filled())
print(c1.get_color())


