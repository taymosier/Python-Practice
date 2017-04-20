'''
Given an array of ints length 3, figure out which is larger, 
the first or last element in the array, and set all the other 
elements to be that value. Return the changed array.
'''
def max_end3(nums):
    larger = max(nums[0],nums[2])
    nums[0] = larger
    nums[1] = larger
    nums[2] = larger
    return nums