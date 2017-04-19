def array_123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

nums_array = [1, 1, 2, 3, 1]

print(array_123(nums_array))