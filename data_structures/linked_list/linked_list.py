from .node import Node


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

    def append(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def insert_before(self, value, new_value):
        current = self.head
        while current.next.data != value:
            current = current.next
        current.next = Node(new_value, current.next)

    def insert_after(self, value, new_value):
        current = self.head
        while current.data != value:
            current = current.next
        current.next = Node(new_value, current.next)

    def ll_kth_from_end(self, value):
        current = self.head
        if len(self) - 1 < value or value < 0:
            return False
        else:
            for _ in range(len(self) - value - 1):
                current = current.next
        return current

    def ll_find_loop(self):
        a = b = self.head
        while a and b and b.next:
            a = a.next
            b = b.next.next
            if a is b:
                return True
        return False
        
    # def ll_find_loop(self):
    #     counter = 0
    #     current = self.head
    #     while current:
    #         current = current.next
    #         counter += 1
    #         if counter > len(self):
    #             return True
    #     return False
