# !/usr/bin/python3.7
"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2010, The Management Tool Project"
__credits__ = ["Prathamesh Rodi"]
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""

from abc import ABCMeta, abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass


# Create concrete classes implementing the same base class.
class Rectangle(Shape):

    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")
    # Create a Factory to generate object of concrete class based on given information.


class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == 'CIRCLE':
            return Circle()
        elif shape_type == 'RECTANGLE':
            return Rectangle()
        elif shape_type == 'SQUARE':
            return Square()
        return None


# Use the Factory to get object of concrete class by passing an information such as type.
if __name__ == '__main__':
    rectangle = ShapeFactory.get_shape('RECTANGLE')
    rectangle.draw()

    circle = ShapeFactory.get_shape('CIRCLE')
    circle.draw()

    square = ShapeFactory.get_shape('SQUARE')
    square.draw()
