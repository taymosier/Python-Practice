string = 'xaxxaxaxx'
count = 0
for i in range(len(string)-2):
    if string[i:i+2] == string[-2:]:
        count = count + 1

print(count)