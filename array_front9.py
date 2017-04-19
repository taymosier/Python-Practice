'''
Given an array of ints, return True if one of the 
first 4 elements in the array is a 9. The array 
length may be less than 4.
'''

def array_front(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False


nums_array = [1, 2, 9, 3, 4]
nums_array2 = [1, 2, 3, 4, 9]

print(array_front(nums_array2))
