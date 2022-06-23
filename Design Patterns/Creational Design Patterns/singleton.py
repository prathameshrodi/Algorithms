# !/usr/bin/python3.7
"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""

class SingletonType(type):
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super(SingletonType, cls).__call__(*args, **kw)
        return cls.instance


class Singleton:
    __metaclass__ = SingletonType

    def do_something(self):
        print('Singleton')


if __name__ == '__main__':
    s = Singleton()
    s.do_something()
