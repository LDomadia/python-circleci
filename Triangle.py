# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Sep 10, 2020

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Leena Domadia
I pledge my Honor that I have abided by the Stevens Honor System
"""

def classify_triangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    if not is_valid_input(a, b, c):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == c and c == a:
        return 'Equilateral'
    if ((a * a) + (b * b)) == (c * c) or ((a * a) + (c * c)) == (b * b) \
            or ((b * b) + (c * c) == (a * a)):
        return 'Right'
    if (a != b) and (b != c) and (a != c):
        return 'Scalene'

    return 'Isosceles'

def is_valid_input(a, b, c):
    """returns boolean whether the input is valid or not"""
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return False

    if a <= 0 or b <= 0 or c <= 0:
        return False

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return False

    return True