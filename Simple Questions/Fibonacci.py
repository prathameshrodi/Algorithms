"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""

def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

