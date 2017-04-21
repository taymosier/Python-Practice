#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            count = count + 1
    return count

word = 'hihi'

print(count_hi('hihi'))