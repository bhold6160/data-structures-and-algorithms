from find_max_value import find_max_value as fmv
from find_max_value import BST as bst
import pytest

@pytest.fixture
def full_tree():
    return bst([3, 8, 10, 35, 68, 4])

def test_fmv_returns_max(full_tree):
    """
    checks the max value
    """
    assert fmv(full_tree) == 68

def test_fmv_returns_after_insert(full_tree):
    """
    Checks max value after new insertion
    """
    full_tree.insert(70)
    assert fmv(full_tree) == 70

def test_fmv_returns_correct(full_tree):
    """
    Checks max value persists after insertion
    """
    full_tree.insert(9)
    assert fmv(full_tree) == 68
