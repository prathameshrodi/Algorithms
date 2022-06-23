# !/usr/bin/python3.7
"""
__author__ = "Prathamesh Rodi"
__copyright__ = "Copyright 2022"
__project__ = "Algorithms"
__version__ = "0.0.1"
__maintainer__ = "Prathamesh Rodi"
__email__ = "prathameshrodi3009@gmail.com"
"""

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Recursive function to calculate height of given binary tree
def height(root):
    # Base case: empty tree has height 0
    if root is None:
        return 0

    # recur for left and right subtree and consider maximum depth
    return 1 + max(height(root.left), height(root.right))


if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    print("The height of the binary tree is", height(root))

    def fibonacci(limit):
        a, b = 0, 1
        while a < limit:
            a, b = b, a + b
        return b
    print(fibonacci())