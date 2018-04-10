from bst import BST as bst


def fizz_buzz_tree(node):
    if node.val % 3 == 0 and node.val % 5 == 0:
        node.val = 'fizzbuzz'
        return node
    elif node.val % 3 == 0:
        node.val = 'fizz'
        return node
    elif node.val % 5 == 0:
        node.val = 'buzz'
        return node
    return
