class CustomList:
    
    def __init__(self, capacity=10):
        self._capacity = capacity  
        self._size = 0  
        self._elements = [None] * self._capacity  
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")
        self.input_numbers()  

    def append(self, element):
        if self._size < self._capacity:
            self._elements[self._size] = element
            self._size += 1
            print(f"Appended {element} to the list.")
        else:
            print("List is full. Cannot append more elements.")

    def get(self, index):
        if 0 <= index < self._size:
            return self._elements[index]
        print(f"Index {index} is out of bounds.")
        return None

    def set(self, index, element):
        if 0 <= index < self._size:
            self._elements[index] = element
            print(f"Set element at index {index} to {element}.")
        else:
            print(f"Index {index} is out of bounds.")

    def size(self):
        return self._size

    def input_numbers(self):
        numbers = input("Enter a set of numbers separated by spaces: ")
        for num in numbers.split():
            try:
                self.append(int(num))
            except ValueError:
                print(f"'{num}' is not a valid integer.")

if __name__ == "__main__":
    custom_list = CustomList()

    custom_list.append(5)  
    print(f"Element at index 0: {custom_list.get(0)}")  
    custom_list.set(0, 10)  # 
    print(f"Element at index 0: {custom_list.get(0)}")  
    print(f"Current size: {custom_list.size()}") \
    



