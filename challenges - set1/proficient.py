"""
Proficiency challenges: Implement a simple binary tree
Challenge 2: Write a function to check if two given binary trees are identical
Challenge 3: Invert a binary tree
"""
class tree_node:
    def __init__(self, data:int=None, left:int=None,right:int=None):
        self.data = data
        self.left = left
        self.right = right

def check_tree(x, y):

	if x is None and y is None:
		raise ValueError('Empty trees given')

	return (x and y) and (x.data == y.data) and check_tree(x.left, y.left) and check_tree(x.right, y.right)


# need to fix invert tree, there is a logic error somewhere
def swap_nodes(tree):
    if tree is None:
        raise ValueError('Empty tree')
    tmp = tree.left
    tree.left = tree.right
    tree.right = tmp

def invert_tree(tree):
    if tree is None:
        raise ValueError('Empty treee')
    swap_nodes(tree)
    invert_tree(tree.left)
    invert_tree(tree.right)
