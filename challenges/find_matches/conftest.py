from .k_tree import KTree as kt
import pytest


@pytest.fixture
def empty_tree():
    return kt()


@pytest.fixture
def full_tree():
    return [1, 2, 3, 4, 5]
