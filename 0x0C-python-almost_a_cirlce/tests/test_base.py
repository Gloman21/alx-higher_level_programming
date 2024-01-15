#!/usr/bin/python3
"""a unittest for base class"""
import unittest
import os
import sys
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """a test class for base class"""

    def test_default(self):
        a1 = Base()
        a2 = Base()
        self.assertEqual(a1.id, a2.id - 1)

    def test_multiple_objects(self):
        a1 = Base()
        a2 = Base()
        a3 = Base()
        self.assertEqual(a1.id, a3.id - 2)

    def test_id_to_none(self):
        a1 = Base(None)
        a2 = Base(None)
        self.assertEqual(a1.id, a2.id - 1)

    def test_custom_id(self):
        a1 = Base(10)
        self.assertEqual(a1.id, 10)

    def test_mixing_deafult_and_custom(self):
        a1 = Base()
        a2 = Base(10)
        a3 = Base()
        self.assertEqual(a1.id, a3.id - 1)

    def test_changing_the_id(self):
        a = Base(10)
        a.id = 100
        self.assertEqual(a.id, 100)

    def test_string_id(self):
        self.assertEqual("Bertin", Base("Bertin").id)

    def test_float_id(self):
        self.assertEqual(2.3, Base(2.3).id)

    def test_dictionary_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_complex_number_id(self):
        self.assertEqual(complex(23), Base(complex(23)).id)

    def test_boolean_id(self):
        self.assertEqual(True, Base(True).id)

    def test_range_id(self):
        self.assertEqual(range(4), Base(range(4)).id)

    def test_many_args_id(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == '__main__':
    unittest.main()
