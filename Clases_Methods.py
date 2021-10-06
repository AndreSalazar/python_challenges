# !/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, side1, side2):
        self.s1 = side1
        self.s2 = side2

    def area(self):
        return self.s1 * self.s2


class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return math.pi * (self.r ** 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()


