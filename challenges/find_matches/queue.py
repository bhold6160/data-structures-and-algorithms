from .node import Node


class Queue:

    def __init__(self, iter=[]):
        """Initializes Queue"""
        self.front = None
        self.back = None
        self._size = 0
        if type(iter) is not list:
            raise TypeError('Invalid iterable')
        for item in iter:
            self.enqueue(item)

    def __len__(self):
        """Returns lenght of queue"""
        return self._size

    def enqueue(self, val):
        """Enqueue node from the back"""
        try:
            node = Node(val)
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
        """Dequeue node from front"""
        dequeued_node = self.front
        self.front = self.front._next
        self._size -= 1
        return dequeued_node.val
