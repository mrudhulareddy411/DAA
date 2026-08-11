def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def find_maximum_after_sorting(nums):
    if not nums:
        return None

    sorted_nums = merge_sort(nums)

    return sorted_nums[-1]


# Test Case 1
print(find_maximum_after_sorting([]))

# Test Case 2
print(find_maximum_after_sorting([5]))

# Test Case 3
print(find_maximum_after_sorting([3, 3, 3, 3, 3]))

# Additional Test Case
print(find_maximum_after_sorting([10, 4, 8, 2, 15]))