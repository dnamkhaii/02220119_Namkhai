class Node:
    def __init__(self, data=None):
        self.data = data  
        self.next = None  

class LinkedQueue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      
        print("Created new LinkedQueue")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def enqueue(self, element):
        new_node = Node(element)  
        if self.is_empty():  
            self.front = self.rear = new_node  
        else:
            self.rear.next = new_node 
            self.rear = new_node  
        self.size += 1
        print(f"Enqueued {element} to the queue")
    
    def dequeue(self):
        if self.is_empty(): 
            print("Queue is empty, cannot dequeue")
            return None
        removed_data = self.front.data  
        self.front = self.front.next 
        if self.front is None:  
            self.rear = None
        self.size -= 1
        print(f"Dequeued element: {removed_data}")
        return removed_data

    def peek(self):
        if self.is_empty():  
            print("Queue is empty, cannot peek")
            return None
        return self.front.data  

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        queue_elements = []
        while current:
            queue_elements.append(str(current.data))
            current = current.next
        print("Display queue: [" + ", ".join(queue_elements) + "]")

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        current = self.front
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> null"

queue = LinkedQueue()
queue.enqueue(10)
queue.display()  
queue.enqueue(20)
queue.display()
queue.enqueue(30)
queue.display()
print("Front element:", queue.peek())
queue.dequeue()
queue.display() 
print(f"Queue size: {queue.get_size()}")


