"""
Use this file to complete the challenges for the week.

After completing the challenges you can run the `run_tests.py` file
to verify your solution works and submit it via our Discord
bot's command `!submit`.
"""

import json
import math
import typing

### Beginner Challenges ###

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def is_even(num: int) -> bool:
    """The `is_even` method for the beginner challenge."""
    return num % 2 == 0


def is_prime(num: int) -> bool:
    """The `is_prime` method for the beginner challenge."""
    return factorial(num - 1) % num != 0


def is_mersenne(num: int) -> bool:
    """The `is_mersenne` method for the beginner challenge."""
    s = 4
    m = (2 ** num) - 1
    for i in range(0, num - 2):
        s = ((s**2) - 2) % m
    return s == 0


### Intermediate Challenges ###


class Car(object):
    def __init__(self, weight: int, wheels: int, passengers: int, model_number: int, car_manufacturer: str):
        self.weight = weight
        self.wheels = wheels
        self.passengers = passengers
        self.model_number = model_number
        self.car_manufacturor = car_manufacturer

    def __repr__(self):
        return f"Car weight: {self.weight} | Car wheels: {self.wheels} | Passengers: {self.passengers} | Model number: {self.model_number}"



### Proficient Challenges ###


class TreeNode(object):
    """A stub class for nodes of a binary tree."""

    def __init__(self, data: typing.Any = None, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        """The stub for the constructor."""
        self.data = data
        self.left = left
        self.right = right




def check_trees(x: TreeNode, y: TreeNode) -> bool:
    """The `check_tree` method for the proficient challenges."""
    if x is None and y is None:
        raise ValueError('Empty trees given')

    return (x and y) and (x.data == y.data) and check_trees(x.left, y.left) and check_trees(x.right, y.right)

def swap_nodes(tree) -> None:
    """The `swap_nodes` method can be used as a helper for `invert_tree`."""
    if tree is None:
        raise ValueError('Empty tree')
    tmp = tree.left
    tree.left = tree.right
    tree.right = tmp


def invert_tree(tree: TreeNode) -> TreeNode:
    """The `invert_tree` method for the proficient challenges."""
    if tree is None:
        raise ValueError('Empty treee')
    swap_nodes(tree)
    invert_tree(tree.left)
    invert_tree(tree.right)
    return tree



### Advanced Challenges ###


def solution(n: int) -> int:
    """The `possible_partitions` method for the advanced challenges."""
    sizearr = n + 1

    # create zero-filled multi_arr
    multi_arr = [[0 for x in range(sizearr)] for n in range(sizearr)]

    # base value is always skipped after being padded
    multi_arr[0][0] = 1
    for last in range(1, sizearr):
        for next in range(0, sizearr):
            multi_arr[last][next] = multi_arr[last - 1][next]
            if next >= last:
                multi_arr[last][next] += multi_arr[last - 1][next - last]

    return multi_arr[n][n] - 1
