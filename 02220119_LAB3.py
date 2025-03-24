class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * self.capacity  # Private array for storage
        self.top = -1  # Variable to track the top of the stack
        print(f"Created new ArrayStack with capacity: {self.capacity}")

    def push(self, element):
        if self.top + 1 == self.capacity:  # Check for stack overflow
            print("Stack overflow! Cannot push.")
            return
        self.top += 1
        self.stack[self.top] = element
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop.")
            return None
        element = self.stack[self.top]
        self.top -= 1
        print(f"Popped element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Display stack:", [self.stack[i] for i in range(self.top + 1)])

if __name__ == "__main__":
    stack = ArrayStack()
    print("Stack is empty:", stack.is_empty())

    stack.push(10)
    stack.display()
    
    stack.push(20)
    stack.display()
    
    stack.push(30)
    stack.display()
    
    print("Top element:", stack.peek())
    
    stack.pop()
    print("Stack size:", stack.size())
    stack.display()