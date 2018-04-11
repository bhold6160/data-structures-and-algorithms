from queue import Queue


class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class BST:
    def __init__(self, iter=[]):
        self.root = None
        if type(iter) is not list:
            raise TypeError
        for item in iter:
            self.insert(item)

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        return self.root.val

    def insert(self, val):
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node

def find_max_value(tree):
    """
    returns max value for binary tree
    """
    queue = Queue()
    max_val = tree.root.val

    queue.enqueue(tree.root)
    while len(queue) > 0:
        current = queue.dequeue()
        if current.val > max_val:
            max_val = current.val
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return max_val
