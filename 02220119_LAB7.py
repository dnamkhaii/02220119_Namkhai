class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value) if value else None

    def height(self):
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def size(self):
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)

    def count_leaves(self):
        def _count_leaves(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return _count_leaves(node.left) + _count_leaves(node.right)
        return _count_leaves(self.root)

    def is_full_binary_tree(self):
        def _is_full(node):
            if not node:
                return True
            if (node.left and not node.right) or (not node.left and node.right):
                return False
            return _is_full(node.left) and _is_full(node.right)
        return _is_full(self.root)

    def is_complete_binary_tree(self):
        def _count_nodes(node):
            if not node:
                return 0
            return 1 + _count_nodes(node.left) + _count_nodes(node.right)
        
        def _is_complete(node, index, node_count):
            if not node:
                return True
            if index >= node_count:
                return False
            return (_is_complete(node.left, 2 * index + 1, node_count) and 
                    _is_complete(node.right, 2 * index + 2, node_count))
        
        if not self.root:
            return True
        return _is_complete(self.root, 0, _count_nodes(self.root))

if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(f"Tree Height: {tree.height()}")
    print(f"Total Nodes: {tree.size()}")
    print(f"Leaf Nodes Count: {tree.count_leaves()}")
    print(f"Is Full Binary Tree: {tree.is_full_binary_tree()}")
    print(f"Is Complete Binary Tree: {tree.is_complete_binary_tree()}")