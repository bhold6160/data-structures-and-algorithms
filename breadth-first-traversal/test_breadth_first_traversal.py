import pytest
from queue import Queue
from breadth_first_traversal import BFT as bft

def test_correct_traversal():
    tree = bft([6, 10, 3, 18, 1])
    assert bft(tree) == [6, 10, 3, 18, 1]
