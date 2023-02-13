#!/usr/bin/python3
"""
Tests for the Place Model
"""


import unittest
import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Reviews"""
    def setUp(self):
        """An instance just for tests"""
        self.a1 = Place()
        self.a2 = Place()

    def test_instances(self):
        """Test the instances"""
        self.assertTrue(isinstance(self.a1, Place))
        self.assertTrue(isinstance(self.a2, Place))
        self.assertTrue(hasattr(self.a1, "name"))


if __name__ == '__main__':
    unittest.main()
