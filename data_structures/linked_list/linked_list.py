from .node import Node


class LinkedList:

    def __init__(self, iter=[]):
        self.head = None
        self._len = 0

        for item in reversed(iter):
            self.head = Node(item, self.head)
            self._len += 1

    def __len__(self):
        """
        Outputs a string to the developer
        """
        return self._len

    def __str__(self):
        """
        Outputs a string to the user
        """
        my_list = []
        current = self.head
        while current:
            my_list.append(current)
            current = current.next
        return str(my_list)

    def insert(self, value):
        """
        Inserts new value to become the head
        """
        self.head = Node(value, self.head)
        self._len += 1

    def find(self, value):
        """
        Finds matching value
        """
        current = self.head
        while current:
            if value == current.data:
                return True
            current = current.next
        return False

    def append(self, value):
        """
        Appends new data to list
        """
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def insert_before(self, value, new_value):
        """
        Inserts new value before the head
        """
        current = self.head
        while current.next.data != value:
            current = current.next
        current.next = Node(new_value, current.next)

    def insert_after(self, value, new_value):
        """
        Inserts new value after the the head
        """
        current = self.head
        while current.data != value:
            current = current.next
        current.next = Node(new_value, current.next)

    # def ll_kth_from_end(self, value):
    #     current = self.head
    #     if len(self) - 1 < value or value < 0:
    #         return False
    #     else:
    #         for _ in range(len(self) - value - 1):
    #             current = current.next
    #     return current

    def ll_kth_from_end(self, data):
        """
        Return the node that is k from the end of the linked list
        """
        if len(self) - data < 0:
            raise AttributeError

        current = self.head
        for i in range(len(self) - data - 1):
            current = current.next
        return current.data

    def ll_find_loop(self):
        """
        Checks linked list for a loop
        """
        a = b = self.head
        while a and b and b.next:
            a = a.next
            b = b.next.next
            if a is b:
                return True
        return False
