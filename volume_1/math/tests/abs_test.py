# import unittest
# import pytest
import math

from dsa_learning.volume_1.math.abs import fabs1

vf = [
    4.9790119248836735e+00,
    7.7388724745781045e+00,
    -2.7688005719200159e-01,
    -5.0106036182710749e+00,
    9.6362937071984173e+00,
    2.9263772392439646e+00,
    5.2290834314593066e+00,
    2.7279399104360102e+00,
    1.8253080916808550e+00,
    -8.6859247685756013e+00
]

fabs = [
    4.9790119248836735e+00,
    7.7388724745781045e+00,
    2.7688005719200159e-01,
    5.0106036182710749e+00,
    9.6362937071984173e+00,
    2.9263772392439646e+00,
    5.2290834314593066e+00,
    2.7279399104360102e+00,
    1.8253080916808550e+00,
    8.6859247685756013e+00
]

signbit = [
    False,
    False,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    True,
]

vfsignbitSC = [
    -math.inf,
    math.copysign(0, -1),
    0,
    math.inf,
    math.nan,
]

signbitSC = [
    True,
    True,
    False,
    False,
    False
]

vffabsSC = [
    -math.inf,
    math.copysign(0, -1),
    0,
    math.inf,
    math.nan
]

fabsSC = [
    math.inf,
    0,
    0,
    math.inf,
    math.nan
]


# https://stackoverflow.com/questions/1986152/why-doesnt-python-have-a-sign-function
# sign_bits return False if x < 0 or negative zero , otherwise return true
def sign_bits(x):
    return math.copysign(1, x) < 0


def test_sign_bits():
    for i in range(len(vf)):
        assert sign_bits(vf[i]) == signbit[i]

    for i in range(len(vfsignbitSC)):
        assert sign_bits(vfsignbitSC[i]) == signbitSC[i]


def alike(num1, num2):
    if math.isnan(num1) and math.isnan(num2):
        return True
    if num1 == num2:
        return sign_bits(num1) == sign_bits(num2)
    return False


def test_abs():
    for i in range(len(vf)):
        assert fabs1(vf[i]) == fabs[i]

    for i in range(len(vffabsSC)):
        assert alike(fabs1(vffabsSC[i]), fabsSC[i])

