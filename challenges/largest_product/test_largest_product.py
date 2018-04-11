from .largest_product import largest_product as lp
import pytest

@pytest.fixture
def arr():
    return [[1, 2], [3, 4], [5, 6], [7, 8]]


def test_largest_product_small(arr):
    """
    test for the largest product
    """
    assert lp(arr) == 56


def test_largest_product_large():
    """
    test for the largest product
    """
    assert lp([[8, 20], [5, 4], [100, 100], [
                           8, 2], [9, 3], [2, 20]]) == 10000


def test_largest_product_medium():
    """
    test for the largest product
    """
    assert lp([[3, 8], [4, 10], [10, 50]]) == 500


