#!/usr/bin/python3
"""Module that provides add_integer function."""


def add_integer(a, b=98):
    """Add two integers.

    a and b must be integers or floats.
    Floats are first cast to integers.

    Raises:
        TypeError: if a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
