class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("Created new LinkedList\nCurrent size: 0\nHead: None")

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def set(self, index, element):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} : {element}")

    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1
        print(f"Prepended {element} to the list")

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Linked list: [" + " ".join(elements) + "]"

linked_list = LinkedList()
linked_list.append(5)
linked_list.get(0)
linked_list.set(0, 6)
print(f"Size: {linked_list.size}")
linked_list.get(0)  
linked_list.prepend(21)
print(linked_list)         