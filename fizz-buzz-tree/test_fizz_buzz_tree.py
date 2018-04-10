import pytest
from bst import BST as bst
from fizz_buzz_tree import fizz_buzz_tree

def test_returns_correct(full_bst):
    assert fizz_buzz_tree(full_bst) == ['fizz', 'buzz', 8, 'fizzbuzz', 'fizzbuzz', 'fizz', 1, 'fizz']

