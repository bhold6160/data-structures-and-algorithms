class Node:

    def __init__(self, value, next=None):
        self.value = value
        self._next = next
        if value is None:
            raise TypeError('Must pass a value')

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)
