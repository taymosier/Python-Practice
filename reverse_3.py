'''
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
'''

def reverse_3(nums):
    temp = nums[0]
    nums[0] = nums[2]
    nums[2] = temp
    return nums