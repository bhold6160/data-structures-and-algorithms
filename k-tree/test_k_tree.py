from k_tree import KTree as kt


def test_single_insert(empty_tree):
    """test insertion into empty tree"""
    empty_tree.insert(empty_tree.root, 4)
    assert empty_tree.root.val == 4


def test_insert_in_filled_tree(filled_tree):
    filled_tree.insert(1, 17)
    assert filled_tree.root.val == 1
