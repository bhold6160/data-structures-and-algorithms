from node import Node


class Stack:
    def __init__(self, iter=[]):
        self.top = None
        self._size = 0

    # We would also define out magics for more info
    def __len__(self):
        return self._size

    def push(self, val):
        try:
            node = Node(val)
        except TypeError:
            print('No value found')
            pass

        node._next = self.top
        self.top = node

        return self.top

    def pop(self):
        pass

    def peek(self):
        pass
