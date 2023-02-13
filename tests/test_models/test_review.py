#!/usr/bin/python3
"""
Tests for the Review Model
"""


import unittest
import datetime

from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Reviews"""
    def setUp(self):
        """An instance just for tests"""
        self.a1 = Review()
        self.a2 = Review()

    def test_instances(self):
        """Test the instances"""
        self.assertTrue(isinstance(self.a1, Review))
        self.assertTrue(isinstance(self.a2, Review))
        self.assertTrue(hasattr(self.a1, "text"))


if __name__ == '__main__':
    unittest.main()
