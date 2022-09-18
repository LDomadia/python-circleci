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
    # your test cases here
    def test1(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
