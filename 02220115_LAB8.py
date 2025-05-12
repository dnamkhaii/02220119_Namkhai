class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Balance cases
        if balance > 1 and key < node.left.key:      # Left Left
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:    # Right Right
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:      # Left Right
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:    # Right Left
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        # Balance cases
        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root)
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root)
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def get_height(self):
        return self._get_height(self.root)

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if not node:
            return True
        balance = self._get_balance(node)
        return abs(balance) <= 1 and self._is_balanced(node.left) and self._is_balanced(node.right)

    # Optional: Print tree (in-order)
    def inorder_traversal(self):
        def _inorder(node):
            return _inorder(node.left) + [node.key] + _inorder(node.right) if node else []
        return _inorder(self.root)

# ==== Example Usage ====
if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)
    avl_tree.insert(25)

    print("In-order Traversal:", avl_tree.inorder_traversal())  # Should be balanced in-order
    print("Is Balanced:", avl_tree.is_balanced())               # True
    print("Tree Height:", avl_tree.get_height())                # Expected: 3

    print("Search 25:", avl_tree.search(25))                    # True
    print("Search 100:", avl_tree.search(100))                  # False

    avl_tree.delete(50)
    print("After Deletion (50), In-order Traversal:", avl_tree.inorder_traversal())
    print("Is Balanced after Deletion:", avl_tree.is_balanced())
    print("Tree Height after Deletion:", avl_tree.get_height())
