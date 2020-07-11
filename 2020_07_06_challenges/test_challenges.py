import unittest
from unittest import mock

import challenges


class T100BeginnerTests(unittest.TestCase):
    """Tests for the beginner challenges."""

    def test_101_is_even(self):
        """Even numbers entered into the function should return `True`, else `False`."""
        self.assertTrue(challenges.is_even(10))
        self.assertFalse(challenges.is_even(11))

    def test_102_is_prime(self):
        """Prime numbers entered into the function should return `True`, else `False`."""
        self.assertTrue(challenges.is_prime(7))
        self.assertFalse(challenges.is_prime(6))

    def test_102_is_mersenne(self):
        """Mersenne primes entered into the function should return `True`, else `False`."""
        self.assertTrue(challenges.is_mersenne(7))
        self.assertFalse(challenges.is_mersenne(8))


class T200IntermediateTests(unittest.TestCase):
    """Tests for the intermediate challenges."""

    def setUp(self):
        self.car_1 = challenges.Car(100, 4, 4, 8649542, "Nissa")
        self.car_2 = challenges.Car(200, 4, 6, 2394583, "Toyota")

    def test_201_car_attributes(self):
        """A car's attributes are set on the instance."""
        self.assertEqual(self.car_1.weight, 100)
        self.assertEqual(self.car_2.weight, 200)

        self.assertEqual(self.car_1.wheels, self.car_2.wheels)

    def test_202_car_str(self):
        """Printing a car should return Car weight : <weight> ¦ Car wheels : <wheels> ¦ Passengers : <passengers> ¦ Model Number : <model_number>."""
        expected_str = f"Car weight: {self.car_1.weight} | Car wheels: {self.car_1.wheels} | Passengers: {self.car_1.passengers} | Model number: {self.car_1.model_number}"
        self.assertEqual(repr(self.car_1), expected_str)


class T300ProficientTests(unittest.TestCase):
    """Tests for the proficient challenges."""

    def setUp(self):
        self.tree_1 = challenges.TreeNode(1, challenges.TreeNode(2), challenges.TreeNode(3))
        self.tree_2 = challenges.TreeNode(1, challenges.TreeNode(2), challenges.TreeNode(3))
        self.tree_3 = challenges.TreeNode(1, challenges.TreeNode(3), challenges.TreeNode(4))
        self.tree_4 = challenges.TreeNode(1, challenges.TreeNode(5), challenges.TreeNode(6))

    def test_301_tree_node(self):
        """`class TreeNode` should be able to take further nodes as well as the `data` attribute."""
        self.assertEqual(self.tree_1.data, 1)
        self.assertEqual(self.tree_1.left.data, 2)
        self.assertEqual(self.tree_1.right.data, 3)

    def test_302_check_tree(self):
        """Check if two trees contain the same data."""
        self.assertTrue(challenges.check_trees(self.tree_1, self.tree_2))
        self.assertFalse(challenges.check_trees(self.tree_1, self.tree_3))
        self.assertFalse(challenges.check_trees(self.tree_1, self.tree_4))
        self.assertFalse(challenges.check_trees(self.tree_3, self.tree_4))

    def test_303_invert_tree(self):
        """Make it possible to invert a tree."""
        res = challenges.invert_tree(self.tree_1)
        self.assertEqual(res.left.data, 3)
        self.assertEqual(res.right.data, 2)


class T400AdvancedTests(unittest.TestCase):
    """Tests for the advanced challenges."""
    pass
