# How to compute the integer absolute value

import math
import cmath
import numpy

# for integer
def abs(num):
    mask = num >> 31
    return (num + mask) ^ mask


# https://graphics.stanford.edu/~seander/bithacks.html#IntegerAbs
# python use 32 bit to represent int http://projectpython.net/chapter02/#integer-types
# https://stackoverflow.com/a/52635807
def fabs1(num):
    mask = num >> 31
    return (num + mask) ^ mask

