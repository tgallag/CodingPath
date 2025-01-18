# Problem: Merge Two Sorted Arrays
'''

Description:
You are given two sorted integer arrays nums1 and nums2, and you need to merge them into a single sorted array.

You must solve this problem without using any built-in sorting methods.

Input:
'''
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

'''
Output:
[1, 2, 3, 4, 5, 6]

'''

s = []
if nums1 != [] and nums2 != []:
    s = nums1 + nums2
    print(sorted(s))
else:
    raise ValueError

# Time Complexity: O((n + m) * log(n + m))
# Space Complexity: O(n + m)