'''

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
'''
def same_first_last(nums):
    if len(nums)<1:
        return False
    elif nums[0] == nums[len(nums)-1]:
        return True
    else:
        return False