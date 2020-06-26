from the_collections import assign_average
import unittest


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(assign_average.switch_average('A'), '90')

    def test_b(self):
        self.assertEqual(assign_average.switch_average('B'), '80')

    def test_c(self):
        self.assertEqual(assign_average.switch_average('C'), '70')

    def test_d(self):
        self.assertEqual(assign_average.switch_average('D'), '60')

    def test_f(self):
        self.assertEqual(assign_average.switch_average('F'), '0')

    def test_z(self):
        self.assertEqual(assign_average.switch_average('Z'), 'Invalid input')
