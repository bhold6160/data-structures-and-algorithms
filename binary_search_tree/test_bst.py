from .bst import BST as bst
import pytest


@pytest.fixture
def left_heavy_tree():
    b = bst()
    b.insert(5)
    b.insert(4)
    b.insert(3)
    b.insert(2)
    b.insert(1)
    return b

@pytest.fixture
def right_heavy_tree():
    b = bst()
    b.insert(1)
    b.insert(2)
    b.insert(3)
    b.insert(4)
    b.insert(5)
    return b

@pytest.fixture
def balanced_tree():
    bal_tree = bst([6, 10, 3, 18, 1])
    return bal_tree


def test_single_insert():
    empty_tree = bst()
    empty_tree.insert(4)
    assert empty_tree.root.val == 4

def test_created_with_iter():
    b = bst([1, 2, 3])
    assert b.root.val == 1
    assert b.root.right.val == 2
    assert b.root.right.right.val == 3

def test_in_order():
    b = bst([2, 3, 1])
    c = []
    b.in_order(lambda n: c.append(n.val))
    assert c == [1, 2, 3]

def test_left_heavy(left_heavy_tree):
    assert left_heavy_tree.root.val == 5
    assert left_heavy_tree.root.left.val == 4
    assert left_heavy_tree.root.left.left.val == 3

def test_right_heavy(right_heavy_tree):
    assert right_heavy_tree.root.val == 1
    assert right_heavy_tree.root.right.val == 2
    assert right_heavy_tree.root.right.right.val == 3

def test_balanced_tree(balanced_tree):
    assert balanced_tree.root.left.val == 3
    assert balanced_tree.root.left.left.val == 1
    assert balanced_tree.root.right.val == 10

def test_pre_order(balanced_tree):
    c = []
    balanced_tree.pre_order(lambda n: c.append(n.val))
    assert c == [6, 3, 1, 10, 18]
    assert balanced_tree.root.right.right.val == 18
    assert balanced_tree.root.left.left.val == 1

def test_post_order(balanced_tree):
    c = []
    balanced_tree.post_order(lambda n: c.append(n.val))
    assert c == [1, 3, 18, 10, 6]
    assert balanced_tree.root.right.val == 10
    assert balanced_tree.root.left.val == 3
