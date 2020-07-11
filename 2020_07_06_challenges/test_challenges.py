import unittest
from unittest import mock

import challenges


class T100BeginnerTests(unittest.TestCase):
    """Tests for the beginner challenges."""

    def test_101_is_even(self):
        self.assertTrue(challenges.is_even(10))
        self.assertFalse(challenges.is_even(11))

    def test_102_is_prime(self):
        self.assertTrue(challenges.is_prime(7))
        self.assertFalse(challenges.is_prime(6))

    def test_102_is_mersenne(self):
        self.assertTrue(challenges.is_mersenne(8))
        self.assertFalse(challenges.is_mersenne(7))
