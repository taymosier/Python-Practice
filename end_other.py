'''

Given two strings, return True if either of the strings appears 
at the very end of the other string, ignoring upper/lower case differences 
(in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.
'''

def end_other(a,b):
    smallerword = min(len(a),len(b))
    if smallerword == len(a):
        return compare_str(b,a)
    elif smallerword == len(b):
        return compare_str(a,b)

def compare_str(longword,shortword):
    if longword[-len(shortword):].lower() == shortword.lower():
        return True
    else:
        return False

print(end_other('Hiabc', 'abc'))