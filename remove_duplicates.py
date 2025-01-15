# Question: Remove Duplicates from Sorted Array
'''
Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

After modifying the array, return the length of the unique elements.

You must do this in-place with O(1) extra space.
'''

nums = [0,0,1,1,1,2,2,4,4,7]

# h = {}  - not needed
# s = ()  - not needed
# seen = []  - not needed


def remove_duplicate():
    write_index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    
    return nums[:write_index]

answer = remove_duplicate()
print(answer)