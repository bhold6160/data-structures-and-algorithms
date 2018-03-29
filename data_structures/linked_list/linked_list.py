from .node import Node


class LinkedList:

    def __init__(self, iter=[]): #Initializing the head 
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
            current = current._next
        return False

    def append(self, value):
        current = self.head
        while current._next:
            current = current._next
        current._next = Node(value)

    def insert_before(self, value, new_value):
        current = self.head
        while current._next != value:
            current = current._next
        current._next = Node(new_value, current._next)

    def insert_after(self, value, new_value):
        current = self.head
        while current != value:
            current._next = Node(new_value, current.next)

    def ll_kth_from_end(self, value):
        current = self.head
        if len(self) - 1 < value or value < 0:
            print('out of range')
            return False
        else:
            for _ in range(value - 1):
                current = current._next
        return current
