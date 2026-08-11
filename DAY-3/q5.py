def large_groups(s):
    result = []
    n = len(s)

    i = 0

    while i < n:
        start = i

        # Find the end of the current group
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1

        end = i

        # Check whether group contains 3 or more characters
        if end - start + 1 >= 3:
            result.append([start, end])

        i += 1

    return result


# Test Case 1
s = "abbxxxxzzy"
print(large_groups(s))


# Test Case 2
s = "abc"
print(large_groups(s))