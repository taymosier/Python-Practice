'''
Return the sum of the numbers in the array, 
except ignore sections of numbers starting 
with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). 
Return 0 for no numbers.
'''

def sum67(nums):
    for i in range(len(nums)):
        if nums[i] == 6:
            nums[i] = 0
            for j in range(len(nums[i:])):
                nums[i+j] = 0
                if nums[i+j+1] == 7:
                    nums[i+j+1] = 0
                    break
    return sum(nums)
