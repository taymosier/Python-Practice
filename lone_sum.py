'''
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as 
another of the values, it does not count towards the sum.
'''

def lone_sum(a,b,c):
    sum = a+b+c
    if a == b and b == c:
        sum = 0
    elif b == c:
        sum = sum - (b*2)
    elif a == b or a == c:
        sum = sum - (a * 2)
    return sum