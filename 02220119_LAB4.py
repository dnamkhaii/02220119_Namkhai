class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        print(f"Created new Queue with capacity: {self.capacity}")

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        if self.size == self.capacity:
            print("Queue is full. Cannot enqueue.")
            return
        self.queue[self.rear] = element
        print(f"Enqueued {element} to the queue")
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        element = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the slot
        print(f"Dequeued element: {element}")
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        self.display()
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[self.front]

    def display(self):
        elements = []
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            elements.append(self.queue[index])
        print(f"Display queue: {elements}")

    def get_size(self):
        return self.size


# Example usage:
if __name__ == "__main__":
    queue = ArrayQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Front element: {queue.peek()}")
    queue.dequeue()
    print(f"Current queue size: {queue.get_size()}")