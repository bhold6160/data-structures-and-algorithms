from linked_list import LinkedList


class HashTable:
    """
    Initialize max size of hash table and creates a linked list for each bucket
    """

    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.buckets = [LinkedList() for _ in range(self.max_size)]

    def hash_key(self, key):
        """
        Converts each character to ascii value and then returns
        remainder after dividing number of buckets by sum and returning
        the location of which bucket will store the value
        """
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

    def set(self, key, val):
        """hashes the key to get a location for the bucket to insert into"""
        return self.buckets[self.hash_key].insert({key: val})

    def get(self, key):
        """Retrieves given key from bucket"""
        bucket = self.buckets[self.hash_key(key)]
        current = bucket.head
        while current:
            if key == current.data[0]:
                return current.data[1]
            current = current.next
        raise KeyError('Does not exist')

    def remove(self, key):
        """Removes given key from bucket"""
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp
