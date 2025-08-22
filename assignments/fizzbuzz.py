"""
This program prints out numbers from 1-30
For numbers divisible by 3 prints out "fizz"
For numbers divisible by 5, prints out "buzz"
For numbers divisible by both, prints out "fizzbuzz"
For all other numbers, print by itself
"""


for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)            


        