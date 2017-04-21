'''
For this problem, we'll round an int value up to the 
next multiple of 10 if its rightmost digit is 5 or more, 
so 15 rounds up to 20. Alternately, round down to the 
previous multiple of 10 if its rightmost digit is less 
than 5, so 12 rounds down to 10. Given 3 ints, a b c,
return the sum of their rounded values. To avoid code 
repetition, write a separate helper "def round10(num):" 
and call it 3 times. Write the helper entirely below 
and at the same indent level as round_sum().
'''

def round_sum(a,b,c):
    a = round10(a)
    b = round10(b)
    c = round10(c)
    return a + b + c

def round10(num):
    if num%10 >= 5:
        num = num + (10-num%10)
    else:
        num = num - num%10
    return num