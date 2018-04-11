class Node:
  def __init__(self, val, next=None):
    self.val = val
    self._next = next


class Queue:

    def __init__(self, iter=[]):
        self.front = None
        self.back = None
        self._size = 0
        if type(iter) is not list:
            raise TypeError('Invalid iterable')
        for item in iter:
            self.enqueue(item)

    def __len__(self):
        return self._size

    def enqueue(self, value):
        try:
            node = Node(value)
        except TypeError:
            return self.back
        self._size += 1
        if self.front is None:
            self.front = node
            self.back = node
        self.back._next = node
        self.back = node
        return self.front

    def dequeue(self):
        dequeued_node = self.front
        self.front = self.front._next
        self._size -= 1
        return dequeued_node.val
