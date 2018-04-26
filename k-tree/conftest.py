from k_tree import KTree as kt
import pytest


@pytest.fixture
def empty_tree():
    return kt()


@pytest.fixture
def filled_tree():
    k = kt()
    k.insert(None, 1)
    k.insert(1, 4)
    k.insert(1, 3)
    k.insert(1, 2)
    k.insert(2, 6)
    k.insert(2, 7)
    k.insert(3, 10)
    k.insert(4, 11)
    return k
