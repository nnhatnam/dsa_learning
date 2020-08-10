# How to compute the integer absolute value

import math
import cmath
import numpy

# https://graphics.stanford.edu/~seander/bithacks.html#IntegerAbs
# python use 32 bit to represent int http://projectpython.net/chapter02/#integer-types
# https://stackoverflow.com/a/52635807
def fabs1(num):
    return math.fabs(num)

