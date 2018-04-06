
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self._next = next

    def __repr__(self):
        return str(self.value)
