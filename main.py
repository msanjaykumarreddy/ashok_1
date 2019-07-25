
""""
create objects and calling methods
"""
from Area_calculations.Area import Differentareacalaculations
from mathoperations.advanced import Advancedmathemeticaloperations
from mathoperations.standard import Standardmathemeticaloperations


class calling():
    pass


a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
length = int(input("Enter length :"))
width = int(input("Enter width :"))
height = int(input("Enter height :"))
AREA_OBJ = Differentareacalaculations(length, width, height)
STANDARD_OBJ = Standardmathemeticaloperations(a, b)
ADVANCED_OBJ = Advancedmathemeticaloperations(a, b)
RESULT_SUB = STANDARD_OBJ.substraction()
RESULT_ADD = STANDARD_OBJ.addition()
RESULT_DIV = STANDARD_OBJ.division()
RESULT_MUL = STANDARD_OBJ.multiplication()
RESULT_SQUARE = ADVANCED_OBJ.square()
RESULT_CUBE = ADVANCED_OBJ.cube()
RESULT_SUAREROOT = ADVANCED_OBJ.squareroot()
RESULT_CUBEROOT = ADVANCED_OBJ.cuberoot()
RESULT_SQUARE_AREA = AREA_OBJ.square_area()
RESULT_RECTANGLE_AREA = AREA_OBJ.rectangle_area()
RESULT_TRIANGLE_AREA = AREA_OBJ.triangle_area()
RESULT_HEXAGON_AREA = AREA_OBJ.hexagon_area()
