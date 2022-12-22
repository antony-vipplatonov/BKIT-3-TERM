import os
import sys
sys.path.append("../lab 2/lab_python_oop")

from rectangle import Rectangle
from circle import Circle
from square import Square

from math import pi
import unittest


class MyTesting(unittest.TestCase):
    def setUp(self):
        self.a = Rectangle('blue', 6, 6)
        self.b = Circle('green', 6)
        self.c = Square('red', 3)

    def test_area(self):
        import math
        self.assertEqual(self.a.square(), 36)
        self.assertEqual(self.b.square(), round(pi * 6**2, 2))
        self.assertEqual(self.c.square(), 9)

    def test_color(self):
        self.assertEqual(self.a.fc.colorproperty, 'blue')
        self.assertEqual(self.b.fc.colorproperty, 'green')
        self.assertEqual(self.c.fc.colorproperty, 'red')

    def test_get_name(self):
        self.assertEqual(self.a.get_figure_type(), 'Прямоугольник')
        self.assertEqual(self.b.get_figure_type(), 'Круг')
        self.assertEqual(self.c.get_figure_type(), 'Квадрат')


if __name__ == '__main__':
    unittest.main()
