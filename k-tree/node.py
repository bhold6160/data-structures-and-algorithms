class Node:

    def __init__(self, val, next=None):
        self.val = val
        self._next = next
        if val is None:
            raise TypeError('Must pass a val')

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)
