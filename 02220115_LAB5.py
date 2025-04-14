def sequential_search(lst, target):
    comparisons = 0
    for index, value in enumerate(lst):  
        comparisons += 1  
        if value == target: 
            return index, comparisons  
    return -1, comparisons  

lst = [23, 45, 12, 67, 89, 34, 56]
target = 67
index, comparisons = sequential_search(lst, target)

# Output
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

print(f"Number of comparisons: {comparisons}")
