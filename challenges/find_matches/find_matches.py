from .node import Node
from .queue import Queue
from .k_tree import KTree


def find_matches(tree, k):
    k = KTree()
    traverse = []

    if k.root is None:
        return traverse
    else:
        for i in k.breadth_first_traversal():
            if k == i.val:
                traverse.append(i.val)
