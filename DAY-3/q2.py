def rob_linear(nums, start, end):
    prev1 = 0
    prev2 = 0

    for i in range(start, end):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current

    return prev1


def rob_houses(nums):
    n = len(nums)

    if n == 0:
        return 0

    if n == 1:
        return nums[0]

    # Case 1: Rob houses from 0 to n-2
    case1 = rob_linear(nums, 0, n - 1)

    # Case 2: Rob houses from 1 to n-1
    case2 = rob_linear(nums, 1, n)

    return max(case1, case2)


# Test Case 1
nums = [2, 3, 2]

print(
    "The maximum money you can rob without alerting the police is",
    rob_houses(nums)
)


# Test Case 2
nums = [1, 2, 3, 1]

print(
    "The maximum money you can rob without alerting the police is",
    rob_houses(nums)
)