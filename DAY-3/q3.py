def climb_stairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second


# Test Case 1
n = 4
print(climb_stairs(n))


# Test Case 2
n = 3
print(climb_stairs(n))