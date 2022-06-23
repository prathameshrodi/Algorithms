# !/usr/bin/python3.7
"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""

from abc import ABCMeta, abstractmethod


# represents the product created by the builder.
class Car(object):
    def __init__(self):
        self.color = None

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return "Car [color={0}]".format(self.color)


# the builder abstraction
class CarBuilder(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def get_result(self):
        pass


class CarBuilderImpl(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_color(self, color):
        self.car.set_color(color)

    def get_result(self):
        return self.car


class CarBuildDirector(object):
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_color("Red")
        return self.builder.get_result()


if __name__ == '__main__':
    builder = CarBuilderImpl()
    carBuildDirector = CarBuildDirector(builder)
    print(carBuildDirector.construct())
