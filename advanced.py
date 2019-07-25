"""
performing advanced math operations
"""
import math
from mathoperations.standard import Standardmathemeticaloperations


class Advancedmathemeticaloperations():
    """
     performing arithmetic operations
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        """
        finding  square of number
        :return:
        """
        result_square = Standardmathemeticaloperations(self.a, self.b).multiplication()
        # print("result_square :", result_square)
        return result_square

    def cube(self):
        """
        finding qube of number
        :return:
        """
        result = Standardmathemeticaloperations(self.a, self.b).multiplication()
        result_cube = result * self.a
        # print("Cube :", result_cube)
        return result_cube

    def squareroot(self):
        """
        finding squareroot of number
        :return:
        """
        result_squareroot = math.sqrt(self.a)
        # result=self.a**0.5
        # print("Squareroot :",result_squareroot)
        return result_squareroot

    def cuberoot(self):
        """
        finding cuberoot of number
        :return:
        """
        # result=math.pow(self.a, 1/3)
        result_cuberoot = self.a ** (1 / 3)
        # print("Cuberoot :", result_cuberoot)
        return result_cuberoot
