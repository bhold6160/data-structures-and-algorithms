from bst import Node, BST


def tree_intersection(tree_one, tree_two):
    empty_set = set()
    set_one = set()
    set_two = set()

    traversed_one = tree_one.pre_order(set_one.add(tree_one.val))
    traversed_two = tree_two.pre_order(set_two.add(tree_one.val))

    for i in traversed_one:
        for j in traversed_two:
            if j == traversed_one[i]:
                empty_set.add(j)
    return empty_set
