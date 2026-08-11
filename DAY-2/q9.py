def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Sorted array
arr = [-9, 3, 4, 6, 8, 9, 10, 30]

# Test Case 1
key = 10
position = binary_search(arr, key)

if position != -1:
    print("Element", key, "is found at position", position + 1)
else:
    print("Element", key, "is not found")


# Test Case 2
key = 100
position = binary_search(arr, key)

if position != -1:
    print("Element", key, "is found at position", position + 1)
else:
    print("Element", key, "is not found") 
