#!/usr/bin/python3
"""Unittests for max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -3, -50, -4]), -3)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-1, 0, 5, 3]), 5)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_none_default_argument(self):
        self.assertIsNone(max_integer())


if __name__ == "__main__":
    unittest.main()
