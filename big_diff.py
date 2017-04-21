'''
Given an array length 1 or more of ints, return the 
difference between the largest and smallest 
values in the array. Note: the built-in min(v1, v2) 
and max(v1, v2) functions return the smaller or larger of two values.
'''

def big_diff(nums):
    minimum = nums[0]
    maximum = nums[0]
    for i in range(len(nums)):
        if minimum > min(minimum,nums[i]):
            minimum = nums[i]
            print('new minimum is ' + str(minimum))
        if maximum < max(maximum,nums[i]):
            maximum = nums[i]
            print('new maximum is ' + str(maximum))
    return maximum - minimum

print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))