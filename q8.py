def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# Test Case 1
arr = [5, 1, 4, 2, 8]
print(bubble_sort(arr))

# Test Case 2
arr = [3, 2, 1]
print(bubble_sort(arr))

# Test Case 3
arr = [1, 2, 3, 4, 5]
print(bubble_sort(arr))