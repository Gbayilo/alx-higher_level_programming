#!/usr/bin/python3
""" Unittests for max_integer([]). """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unitteses for max_integer([]). """

    def test_empty_list(self):
        """ Test an empty list """
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """ test list of one element """
        self.assertEqual(max_integer([8]), 8)

    def test_ordered_list(self):
        """ Test an ordered list """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """ Test an unorderd list """
        self.assertEqual(max_integer([7, 3, 2]), 7)

    def test_negative_numbers(self):
        """ test negative numbers """
        self.assertEqual(max_integer([-3, -4, -1]), -1)

    def test_mixed_numbers(self):
        """ tes mixed numbers """
        self.assertEqual(max_integer([6, -8, -4, 14]), 14)

    def test_float(self):
        """ test float """
        self.assertEqual(max_integer([4.14, -6.1, 8, 0, 12]), 12)

    def test_string(self):
        """ test string """
        self.assertEqual(max_integer("green"), 'r')

    def test_list_of_strings(self):
        """ test a list of strings """
        self.assertEqual(max_integer(["game", "aim", "broom"]), "game")


if __name__ == '__main__':
    unittest.main()
