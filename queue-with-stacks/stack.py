from node import Node

class Stack:
    def __init__(self, iter=[]):
        self.top = None
        self._len = 0

        for item in iter:
            self.push(item)

    def __len__(self):
        return self._len

    def __str__(self):
        my_list = ''
        current = self.top
        while current:
            print(current.value)
            my_list += str(current.value) + ' '
            current = current._next
        return my_list

    def push(self, value):
        self.top = Node(value, self.top)
        self._len += 1

    def pop(self):
        if len(self) == 0:
            raise IndexError('nothing found')
        if len(self) == 1:
            current = self.top
            self.top = None
            return current.value

    def peek(self):
        if len(self) == 0:
            raise IndexError('nothing found')
        else:
            return self.top


        