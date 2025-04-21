def merge_sort(arr):
    comparisons = 0
    accesses = 0

    def merge(left, right):
        nonlocal comparisons, accesses
        sorted_array = []
        i = j = 0

        while i < len(left) and j < len(right):
            accesses += 2  # Accessing left[i] and right[j]
            comparisons += 1  # Comparison between left[i] and right[j]

            if left[i] <= right[j]:
                sorted_array.append(left[i])
                accesses += 1  # Accessing left[i]
                i += 1
            else:
                sorted_array.append(right[j])
                accesses += 1  # Accessing right[j]
                j += 1

        while i < len(left):
            sorted_array.append(left[i])
            accesses += 1  # Accessing left[i]
            i += 1

        while j < len(right):
            sorted_array.append(right[j])
            accesses += 1  # Accessing right[j]
            j += 1

        return sorted_array

    def sort(array):
        nonlocal comparisons, accesses
        if len(array) <= 1:
            accesses += 1  
            return array
        
        mid = len(array) // 2
        left_half = sort(array[:mid])
        right_half = sort(array[mid:])

        return merge(left_half, right_half)

    sorted_array = sort(arr)
    return sorted_array, comparisons, accesses

if __name__ == "__main__":
    original_list = [38, 27, 43, 3, 9, 82, 10]
    sorted_list, num_comparisons, num_accesses = merge_sort(original_list)

    print("Original List:", original_list)
    print("Sorted using Merge Sort:", sorted_list)
    print("Number of comparisons:", num_comparisons)
    print("Number of array accesses:", num_accesses)