class Animal:
    def __init__(self, back, front):
        self.back = back
        self.front = front
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, animal):
        self.enqueue(animal)
        return self.back

    def dequeue(self, animal, default=None):
        current = self.front
        adopted_animal = None
        if user_input == None or user_input == self.back.value:
            return self.front.next
        while current.next is not None:
            if current.next.value == animal:
                adopted_animal = current.next
                current.next = current.next.next
                return adopted_animal
            current = current.next
        return adopted_animal
