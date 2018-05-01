from node import Node


class LinkedList:

    def __init__(self, iter=[]):
        self.head = None
        self._len = 0

        for item in reversed(iter):
            self.head = Node(item, self.head)
            self._len += 1

    def __len__(self):
        return self._len

    def __str__(self):
        my_list = []
        current = self.head
        while current:
            my_list.append(current)
            current = current.next
        return str(my_list)

    def insert(self, value):
        self.head = Node(value, self.head)
        self._len += 1

    def find(self, value):
        current = self.head
        while current:
            if value == current.data:
                return True
            current = current.next
        return False
