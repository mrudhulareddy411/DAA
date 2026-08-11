def unique_paths(m, n):
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]

    return dp[n - 1]


# Test Case 1
m = 7
n = 3

print(unique_paths(m, n))


# Test Case 2
m = 3
n = 2

print(unique_paths(m, n))