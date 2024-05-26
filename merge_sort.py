def merge_sort(strings):
    if len(strings) <= 1:
        return strings

    mid = len(strings) // 2
    left_half = merge_sort(strings[:mid])
    right_half = merge_sort(strings[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    while left and right:
        if len(left[0]) > len(right[0]):
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    
    sorted_list.extend(left if left else right)
    return sorted_list

# Test the modified Merge sort algorithm against 3 string lists
list1 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
list2 = ["cucumber", "pepper", "carrot", "lettuce", "broccoli", "spinach", "tomato", "celery", "onion", "garlic"]
list3 = ["dolphin", "whale", "shark", "octopus", "jellyfish", "squid", "lobster", "crab", "seahorse", "starfish"]

sorted_list1 = merge_sort(list1)
sorted_list2 = merge_sort(list2)
sorted_list3 = merge_sort(list3)

print("Sorted List 1:", sorted_list1)
print("Sorted List 2:", sorted_list2)
print("Sorted List 3:", sorted_list3)
