from .node import Node


class Stack:
    def __init__(self, iter=[]):
        self.top = None
        self._size = 0

    # We would also define out magics for more info

    def __repr__(self):
        return f'Top stack is  {self.top.value}'

    def __len__(self):
        return self._size

    def push(self, value):
        try:
            node = Node(value)
        except TypeError:
            print('No value found')
            return self.top
        self._size += 1
        node._next = self.top
        self.top = node
        return self.top

    def pop(self):
        remove_node = self.top
        self.top = self.top._next
        self._size -= 1
        return remove_node

    def peek(self):
        assert self.top.value