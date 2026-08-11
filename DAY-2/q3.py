def sum_of_distinct_squares(nums):
    n = len(nums)
    total = 0

    for i in range(n):
        distinct = set()

        for j in range(i, n):
            distinct.add(nums[j])
            count = len(distinct)
            total += count * count

    return total


# Test Case 1
nums = [1, 2, 1]
print(sum_of_distinct_squares(nums))

# Test Case 2
nums = [1, 1]
print(sum_of_distinct_squares(nums))
