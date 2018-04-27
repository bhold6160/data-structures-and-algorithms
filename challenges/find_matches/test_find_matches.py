import pytest


def test_single_insert(empty_tree):
    """test insertion into empty tree"""
    empty_tree.insert(empty_tree.root, 4)
    assert empty_tree.root.val == 4


def test_find_match(full_tree):
    full_tree.find_matches(2)
    assert find_matches == 1
