from node import Node, BST
from sets import Set


def tree_intersection(tree_one, tree_two):
    empty_list = []
    set_one = Set([tree_one])
    set_two = Set([tree_two])

    for i in set_one:
        for j in set_two:
            if j == set_one[i]:
                empty_list.append(j)
    return empty_list
