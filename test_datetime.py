from the_collections import half_birthday
import unittest
import datetime


class TestStringMethods(unittest.TestCase):
    def test_hb(self):
        self.assertEqual(half_birthday.half_birthday(2003, 2, 20), datetime.datetime(2003, 8, 20))
