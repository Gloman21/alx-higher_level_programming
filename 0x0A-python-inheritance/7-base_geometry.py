#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Deals with geometry areas.."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
