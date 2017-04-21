'''
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming 
we always use big bars before small bars. Return -1 if it can't be done.
'''

def make_chocolate(small, big, goal):
    goal = use_big_chocolate(big,goal)
    if goal == 0:
        return 0
    return use_small_chocolate(small,goal)

def use_big_chocolate(big,goal):
    while goal >= 5 and big > 0:
        big = big - 1
        goal = goal - 5
    return goal

def use_small_chocolate(small,goal):
    count = 0
    if goal <= small:
        count = small - (small - goal)
    elif goal > small:
        count = -1
    return count

print(make_chocolate(4,1,5))
