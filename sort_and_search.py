# Implementing Linear Search to find the number 9
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Linear Search explanation:
# Linear Search is chosen here because the list is unsorted. It sequentially checks each element
# and is simple to implement for small to moderately sized lists.

# Implementing Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Implementing Binary Search on a sorted array to find the number 9
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Binary Search explanation:
# Binary Search is efficient for sorted lists as it repeatedly divides the search interval in half.
# It's much faster than Linear Search for large lists, with a time complexity of O(log n).

# Given list
arr = [4, 2, 7, 1, 9, 3, 6, 8, 5, 10]

# Linear Search for number 9
index = linear_search(arr, 9)
print("Linear Search: Number 9 is at index", index)

# Sorting the array using Insertion Sort
sorted_arr = insertion_sort(arr)
print("Sorted Array:", sorted_arr)

# Binary Search for number 9 in the sorted array
index = binary_search(sorted_arr, 9)
print("Binary Search: Number 9 is at index", index)
