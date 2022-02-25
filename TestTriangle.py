# -*- coding: utf-8 -*-
"""
Updated Sep 10, 2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Leena Domadia
I pledge my Honor that I have abided by the Stevens Honor System
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTrianglesA(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classify_triangle(200, 200, 200),'Equilateral','200,200,200 should be equilateral')

    def testInvalidInputA(self):
        self.assertEqual(classify_triangle(201, 201, 201), 'InvalidInput', '201,201,201 should be invalid input')

    def testInvalidInputB(self):
        self.assertEqual(classify_triangle(3, 0, 5), 'InvalidInput', '3,0,5 should be invalid input')

    def testInvalidInputC(self):
        self.assertEqual(classify_triangle(7.5, 6, 5), 'InvalidInput', '7.5,6,5 should be invalid input')

    def testInvalidInputD(self):
        self.assertEqual(classify_triangle(-4, 3, 5), 'InvalidInput', '-4,3,5 should be invalid input')

    def testInvalidInputE(self):
        self.assertEqual(classify_triangle(201, 199, 199), 'InvalidInput', '201,199,199 should be invalid input')

    def testNotATriangleA(self):
        self.assertEqual(classify_triangle(7, 4, 1), 'NotATriangle', '7,4,1 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classify_triangle(5, 2, 3), 'NotATriangle', '5,2,3 is not a triangle')

    def testIsoscelesA(self):
        self.assertEqual(classify_triangle(3, 5, 3), 'Isosceles', '3,5,3 is isosceles')

    def testIsoscelesB(self):
        self.assertEqual(classify_triangle(3, 3, 5), 'Isosceles', '3,3,5 is isosceles')

    def testIsoscelesC(self):
        self.assertEqual(classify_triangle(5, 3, 3), 'Isosceles', '5,3,3 is isosceles')

    def testScaleneA(self):
        self.assertEqual(classify_triangle(6, 3, 5), 'Scalene', '6,3,5 is scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
