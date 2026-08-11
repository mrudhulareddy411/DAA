def unique_elements(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


# Test Case 1
nums = [3, 7, 3, 5, 2, 5, 9, 2]
print(unique_elements(nums))

# Test Case 2
nums = [-1, 2, -1, 3, 2, -2]
print(unique_elements(nums))

# Test Case 3
nums = [1000000, 999999, 1000000]
print(unique_elements(nums))