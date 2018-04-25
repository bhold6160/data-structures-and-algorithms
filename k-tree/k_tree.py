from node import Node


class KTree:
    def __init__(self):
        """Initializes Ktree class"""
        self.root = None
        self._size = 0

    def __repr__(self):
        """Represents tree root"""
        return '<KTree Root {}>'.format(self.root.val)

    def __str__(self):
        """String of root value"""
        return self.root.val

    def pre_order(self, operation):
        """Pre-order traversal"""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            for children in node.children:
                _walk(children)

        _walk(self.root)

    def post_order(self, operation):
        """Post-order traversal"""
        def _walk(node=None):
            if node is None:
                return

            for children in node.children:
                _walk(children)

            operation(node)

        _walk(self.root)

    def insert(self, parent, val):
        """Insert value into tree at parent"""
        if not self.root:
            self.root = Node(val)
            self._size += 1
        else:
            def insert(node):
                if node.val == parent:
                    node.insert(val)
                    self._size += 1
            self._breadth_first(insert)

