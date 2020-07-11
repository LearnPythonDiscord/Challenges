"""
Use this file to complete the challenges for the week.

After completing the challenges you can run the `run_tests.py` file
to verify your solution works and submit it via our Discord
bot's command `!submit`.
"""

import json
import math

### Beginner Challenges ###


def is_even(num: int) -> bool:
    """The `is_even` method for the beginner challenge."""
    pass


def is_prime(num: int) -> bool:
    """The `is_prime` method for the beginner challenge."""
    pass


def is_mersenne(num: int) -> bool:
    """The `is_mersenne` method for the beginner challenge."""
    pass


### Intermediate Challenges ###


class Car(object):
    """The `Car` class you need to write for the intermediate challenge."""

    def __init__(self, weight, wheels, passengers, model_number, manufacturer):
        """The stub for the constructor. Introduce type-hinting as part of the challenge."""
        pass

    def __str__(self):
        """This method needs to be overriden as part of the challenge."""
        pass


### Proficient Challenges ###


class TreeNode(object):
    """A stub class for nodes of a binary tree."""

    def __init__(self, data: Any = None, left: TreeNode = None, right: TreeNode = None):
        """The stub for the constructor."""
        pass


def check_tree(x: TreeNode, y: TreeNode) -> bool:
    """The `check_tree` method for the proficient challenges."""
    pass


def swap_nodes(tree: TreeNode) -> TreeNode:
    """The `swap_nodes` method can be used as an extension for the `invert_tree`."""
    pass


def invert_tree(tree: TreeNode) -> TreeNode:
    """The `invert_tree` method for the proficient challenges."""
    pass


### Advanced Challenges ###


def possible_partitions(n: int) -> int:
    """The `possible_partitions` method for the advanced challenges."""
    pass
