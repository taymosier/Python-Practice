'''
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
'''
def count_evens(nums):
    count = 0
    for i in (nums):
        if i % 2 == 0:
            count = count + 1
    return count
print(count_evens([2, 1, 2, 3, 4]))