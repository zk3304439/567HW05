# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle1 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(6,8,10), 'Right', '6,8,10 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(10,6,8), 'Right', '10,6,8 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(3,3,3), 'Equilateral', '1,1,1 should be Equilateral')
        self.assertEqual(classifyTriangle(10,10,10), 'Equilateral', '10,10,10 Should be Equilateral')

    def testotherTriangles(self):
        self.assertEqual(classifyTriangle(15, 16, 30), 'Scalene', '15,16,30 Should be Scalene')
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isosceles', '1,2,2 should be Isosceles')
        self.assertEqual(classifyTriangle(1, 2, 5), 'NotATriangle', '1,2,5 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

