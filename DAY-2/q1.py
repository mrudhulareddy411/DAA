def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""


# Test Case 1
words1 = ["abc", "car", "ada", "racecar", "cool"]
print(first_palindrome(words1))

# Test Case 2
words2 = ["notapalindrome", "racecar"]
print(first_palindrome(words2))
