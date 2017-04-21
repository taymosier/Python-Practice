'''
Return the "centered" average of an array of ints, which we'll say is 
the mean average of the values, except ignoring the largest and smallest 
values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division 
to produce the final average. You may assume that the array is length 3 or more.
'''
def centered_average(nums):
    minimum = nums[0]
    maximum = nums[0]

    for i in range(len(nums)):
        if maximum < max(maximum,nums[i]):
            maximum = nums[i]
        if minimum > min(minimum,nums[i]):
            minimum = nums[i]
    summedlist = sum(nums) - minimum - maximum

print(int(-16/6))