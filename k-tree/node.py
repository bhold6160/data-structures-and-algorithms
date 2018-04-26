class Node:

    def __init__(self, val):
        """Initializes node"""
        self.val = val
        self.child = None
        self.children = []

    def __repr__(self):
        """Represents node value"""
        return 'Node value {}' .format(self.val)

    def __str__(self):
        """string of node value"""
        return self.val
