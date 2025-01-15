# Question: Remove Duplicates from Sorted Array
'''
Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

After modifying the array, return the length of the unique elements.

You must do this in-place with O(1) extra space.
'''

nums = [0,0,1,1,1,2,2,3,3,4]

h = {}

def remove_duplicate():
    for num in nums:
        i= 0
        if num == h[num]:
            i += 1
            print(i)
        else:
            print("not working")
            break

remove_duplicate()