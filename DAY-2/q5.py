def find_maximum(nums):
    if not nums:
        return None

    maximum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num

    return maximum


# Test Case 1
nums = [1, 2, 3, 4, 5]
print(find_maximum(nums))

# Test Case 2
nums = [7, 7, 7, 7, 7]
print(find_maximum(nums))

# Test Case 3
nums = [-10, 2, 3, -4, 5]
print(find_maximum(nums))v
