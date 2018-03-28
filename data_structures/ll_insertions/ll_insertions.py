from node import Node

class LinkedList:

    def __init__(self, iter = []):
        self.head = None
        self._len = 0
    
        for item in iter:
            self.head = Node(item, self.head)
            self._len += 1

    def __len__(self):
        return self._len

    def __str__(self):
        my_list = []
        current = self.head
        for _ in range(self._len+1):
            my_list.append(current)
            current = current._next
        return str(my_list)
    
    def insert(self, value):
        self.head = Node(value, self.head)
        self._len += 1

    def find(self, value):
        if self.head == None:
            return False
        elif self.head == value:
            return True
        else:
            current = self.head
            next = current._next
            if next.data == value:
                return True
            else:
                while next.data != value and next is not None:
                    current = next
                    next = current._next
                if next.data == value:
                    return True
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
                