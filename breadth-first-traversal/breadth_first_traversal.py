class Node(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def breadth_first_traversal(root):
  current = [root]
  while current:
    next_node = list()
    for node in current:
      print(node.val),
      if node.left:
        next_node.append(node.left)
      if node.right:
        next_node.append(node.right)
    print
    current = next_node
