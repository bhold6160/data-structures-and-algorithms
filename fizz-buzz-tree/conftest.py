import pytest
from bst import BST as bst

@pytest.fixture
def empty_bst():
    """ 
    returns empty tree
    """
    return bst()

@pytest.fixture
def full_bst():
    """ 
    creates a tree with values to check
    """
    return bst([3, 5, 8, 15, 30, 12, 1, 21])


