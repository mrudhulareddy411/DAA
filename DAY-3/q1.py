def find_paths(m, n, N, i, j):
    MOD = 1000000007

    # dp[r][c] = number of ways to reach cell (r,c)
    dp = [[0] * n for _ in range(m)]
    dp[i][j] = 1

    result = 0

    for step in range(N):
        new_dp = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue

                # Up
                if r == 0:
                    result = (result + dp[r][c]) % MOD
                else:
                    new_dp[r - 1][c] = (new_dp[r - 1][c] + dp[r][c]) % MOD

                # Down
                if r == m - 1:
                    result = (result + dp[r][c]) % MOD
                else:
                    new_dp[r + 1][c] = (new_dp[r + 1][c] + dp[r][c]) % MOD

                # Left
                if c == 0:
                    result = (result + dp[r][c]) % MOD
                else:
                    new_dp[r][c - 1] = (new_dp[r][c - 1] + dp[r][c]) % MOD

                # Right
                if c == n - 1:
                    result = (result + dp[r][c]) % MOD
                else:
                    new_dp[r][c + 1] = (new_dp[r][c + 1] + dp[r][c]) % MOD

        dp = new_dp

    return result


# Test Case 1
m = 2
n = 2
N = 2
i = 0
j = 0

print(find_paths(m, n, N, i, j))


# Test Case 2
m = 1
n = 3
N = 3
i = 0
j = 1

print(find_paths(m, n, N, i, j))