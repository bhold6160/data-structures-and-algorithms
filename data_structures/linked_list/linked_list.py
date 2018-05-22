from node import Node


class LinkedList:
    def __init__(self, iterable=[]):
        """Construct new LinkedList."""
        self.head = None
        self.length = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def __len__(self):
        """Overwrite the default return for len function."""
        return self.length

    def __str__(self):
        """Overwrite the default return for print function."""
        return self.display()

    def size(self):
        """Get the size of the LinkedList."""
        return len(self)

    def push(self, val):
        """Add new value to the front of the list."""
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        if not self.head:
            raise IndexError('Cannot pop from empty list')
        val = self.head.val
        self.head = self.head.next
        self.length -= 1
        return val

    def search(self, val):
        """Find node containing given value."""
        current = self.head

        while current:
            if current.val == val:
                return current
            current = current.next

    def remove(self, node):
        """Remove given node from LinkedList."""
        if self.head is node:
            self.head = self.head.next
            self.length -= 1
            return

        current = self.head
        while current:
            if current.next is node:
                current.next = node.next
                self.length -= 1
                return
            current = current.next

        raise ValueError('Node does not exist')
