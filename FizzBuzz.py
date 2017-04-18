#Prints 'fizz' if input is divisible by 3, 'buzz' if divisible by 5, and 'fizzbuzz' if divisible by both 3 and 5.

from random import randint

input = randint

print("The number is " + str(input))

if(input % 3 == 0) and (input % 5 == 0):
        print("Fizzbuzz")
elif(input %3 == 0):
        print("Fizz")
elif(input % 5 == 0):
        print("Buzz")
else:
     print("This number is not divisible by 3 or 5")


