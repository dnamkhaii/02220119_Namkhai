class Node:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color  # 'red' or 'black'
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(value=None, color='black')  # Sentinel node
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        self._insert_node(new_node)
        self._fix_insert(new_node)
        print(f"Inserted: {value}")

    def _insert_node(self, new_node):
        parent = None
        current = self.root
        
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        
        if parent is None:  # Tree was empty
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:  # Parent is a left child
                uncle = node.parent.parent.right
                if uncle.color == 'red':  # Case 1
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:  # Case 2 and 3
                    if node == node.parent.right:  # Case 3
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = 'black'  # Case 2
                    node.parent.parent.color = 'red'
                    self._rotate_right(node.parent.parent)
            else:  # Parent is a right child
                uncle = node.parent.parent.left
                if uncle.color == 'red':  # Case 1
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:  # Case 2 and 3
                    if node == node.parent.left:  # Case 3
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = 'black'  # Case 2
                    node.parent.parent.color = 'red'
                    self._rotate_left(node.parent.parent)
        
        self.root.color = 'black'

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y

    def delete(self, value):
        node_to_delete = self.search_node(value)
        if node_to_delete == self.NIL:
            print(f"Value {value} not found for deletion.")
            return 

        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self._transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self._transplant(node_to_delete, node_to_delete.left)
        else:
            y = self._minimum(node_to_delete.right)
            original_color = y.color
            x = y.right
            if y.parent == node_to_delete:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y
            self._transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.color = node_to_delete.color

        if original_color == 'black':
            self._fix_delete(x)

        print(f"Deleted: {value}")

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = 'black'

    def search(self, value):
        found = self.search_node(value) != self.NIL
        print(f"Searched for: {value}, Found: {found}")
        return found

    def search_node(self, value):
        current = self.root
        while current != self.NIL:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return self.NIL

    def get_black_height(self):
        height = self._black_height(self.root)
        print(f"Black height of the tree: {height}")
        return height

    def _black_height(self, node):
        if node == self.NIL:
            return 1
        left_black_height = self._black_height(node.left)
        right_black_height = self._black_height(node.right)
        if left_black_height != right_black_height:
            raise ValueError("Red-Black Tree property violated.")
        return left_black_height + (1 if node.color == 'black' else 0)

    def print_tree(self):
        print("In-order Traversal of the Tree:")
        self._in_order_traversal(self.root)
        print()  

    def _in_order_traversal(self, node):
        if node != self.NIL:
            self._in_order_traversal(node.left)
            print(f"{node.value} ({node.color})", end=" ")
            self._in_order_traversal(node.right)

rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)
rb_tree.get_black_height()  
rb_tree.print_tree()  
rb_tree.search(20)
rb_tree.delete(20)
rb_tree.get_black_height()  
rb_tree.print_tree()  
rb_tree.search(20)