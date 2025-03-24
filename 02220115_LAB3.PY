class Node:
    def __init__(self, data=None):
    
        self.data = data  
        self.next = None  

class LinkedStack:
    def __init__(self):
        
        self.top = None  
        self.size = 0  


    def push(self, element):
       
        new_node = Node(element)  
        new_node.next = self.top  
        self.top = new_node  
        self.size += 1  
        print(f"Pushed {element} to the stack")

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Display stack:", elements)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_element = self.top.data  
        self.top = self.top.next  
        self.size -= 1  
        print(f"Popped element: {popped_element}")
        return popped_element
    
    def peek(self):
        """Return the element at the top of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.top.data
    
    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

linked_stack = LinkedStack()
linked_stack.push(10)
linked_stack.display()
linked_stack.push(20)
linked_stack.display()
linked_stack.push(30)
linked_stack.display()
print("Top element:", linked_stack.peek())
linked_stack.pop()
linked_stack.display()
print(f"Stack size: {linked_stack.size}")


