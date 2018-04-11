import pytest
from queue import Queue
from breadth_first_traversal import BST as bst
from breadth_first_traversal import breadth_first_traversal as bft

def test_correct_traversal():
    tree = bst([6, 10, 3, 18, 1])
    assert bft(tree) == [6, 10, 3, 18, 1]
