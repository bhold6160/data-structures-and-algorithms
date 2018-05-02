from bst import Node, BST


def tree_intersection(tree_one, tree_two):
    b = BST()
    n = Node()
    empty_set = set()
    set_one = set()
    set_two = set()

    traversed_one = b.pre_order(set_one.add(tree_one))
    traversed_two = b.pre_order(set_two.add(tree_one))

    for i in traversed_one:
        for j in traversed_two:
            if traversed_one[i] == traversed_two[j]:
                empty_set.add(j.val)
    return empty_set
