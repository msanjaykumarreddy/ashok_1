"""
performing area operations
"""
from mathoperations.standard import Standardmathemeticaloperations


class Differentareacalaculations:
    """
finding area calculations
    """

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def square_area(self):
        """
        finding the area of the square
        :return:
        """
        area_sqaure = Standardmathemeticaloperations(self.length, self.width).multiplication()
        print("Area of the square :", area_sqaure)
        return area_sqaure

    def triangle_area(self):
        """
        finding the area of the triangle
        :return:
        """
        res_add = Standardmathemeticaloperations(self.length, self.width).addition()
        s = Standardmathemeticaloperations(res_add, self.height).addition() / 2
        area_triangle = (s * (s - self.length) * (s - self.width) * (self.height)) ** 0.5
        print("Area of the triangle :", area_triangle)
        return area_triangle

    def rectangle_area(self):
        """
        finding the area of rectangle
        :return:
        """
        area_rectangle = self.length * self.width
        print("Area of the rectangle :", area_rectangle)
        return area_rectangle

    def hexagon_area(self):
        """
        finding the area of  hexagon
        :return:
        """
        area_hexagon = ((self.length * self.length) ** (1 / 3)) / 2
        print("Area of the hexagon :", area_hexagon)
        return area_hexagon
