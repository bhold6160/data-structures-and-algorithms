class Node:

    def __init__(self, data, next=None):
        self.data = data
        self._next = next

    def __repr__(self):
        return str(self.data)
