#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """Class for BaseGeometry"""

    def area(self):
        """Method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate integer"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
