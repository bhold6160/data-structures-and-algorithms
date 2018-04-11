import pytest
from breadth_first_traversal import breadth_first_traversal as bft

@pytest.fixture
def balanced_tree():
    bal_tree = bst([6, 10, 3, 18, 1])
    return bal_tree

def test_correct_traversal():
    pass