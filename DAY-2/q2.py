def find_intersection_values(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = sum(1 for x in nums1 if x in set2)
    answer2 = sum(1 for x in nums2 if x in set1)

    return [answer1, answer2]


# Test Case 1
nums1 = [2, 3, 2]
nums2 = [1, 2]
print(find_intersection_values(nums1, nums2))

# Test Case 2
nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]
print(find_intersection_values(nums1, nums2))
