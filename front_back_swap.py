'''
Given a string, return a new string where the first and last chars have been exchanged.
'''

def front_back(str):
    if len(str) < 2:
        return str
    else:
        str = list(str)
        temp = str[0]
        str[0] = str[len(str) - 1]
        str[len(str) - 1] = temp
        return ''.join(str)