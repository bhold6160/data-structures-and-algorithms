import largest_product.largest_product as lp
import pytest

@pytest.fixture
def arr():
    return [[1, 2], [3, 4], [5, 6], [7, 8]]

def test_largest_product_not():
    assert lp.largest_product([0]) == 0

def test_largest_product():
    assert lp.largest_product(arr) == 56
