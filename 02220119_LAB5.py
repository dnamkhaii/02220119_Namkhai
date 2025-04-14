def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1, comparisons

def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons
        
    mid = (left + right) // 2
    comparisons += 1
    
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)

def main():
    arr = [12, 23, 34, 45, 56, 67, 89]
    target = 12
    
    print(f"Sorted List: {arr}")
    print(f"Searching for {target} using Binary Search")
    
    #iterative method
    index, comparisons = binary_search_iterative(arr, target)
    if index != -1:
        print(f"Iterative - Found at index {index}")
        print(f"Iterative - Number of comparisons: {comparisons}")
    else:
        print("Iterative - Target not found")
        
    #recursive method
    index, comparisons = binary_search_recursive(arr, target, 0, len(arr)-1)
    if index != -1:
        print(f"Recursive - Found at index {index}")
        print(f"Recursive - Number of comparisons: {comparisons}")
    else:
        print("Recursive - Target not found")

if __name__ == "__main__":
    main()
    