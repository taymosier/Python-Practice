#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    catcount = 0
    dogcount = 0
    for i in range(len(str)-2):
        if str[i:i+3] == 'cat':
            catcount = catcount + 1
        elif str[i:i+3]  == 'dog':
            dogcount = dogcount + 1
    if dogcount == catcount:
        return True
    else:
        return False

