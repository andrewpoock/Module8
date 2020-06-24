from the_collections import set_membership
import unittest


class TestStringMethods(unittest.TestCase):
    def test_true(self):
        self.assertTrue(set_membership.in_set(3, {1, 2, 3}))

    def test_false(self):
        self.assertFalse(set_membership.in_set(5, {1, 2, 3}))
