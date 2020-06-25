from the_collections import dict_membership
import unittest


class TestStringMethods(unittest.TestCase):
    def test_true(self):
        self.assertTrue(dict_membership.in_dict('B', {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}))

    def test_false(self):
        self.assertFalse(dict_membership.in_dict('G', {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}))
