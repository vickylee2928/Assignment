"""
ODD OR EVEN GAME
This program checks if a user-input number is odd or even.
-The user enters a number
-The program determines if it's divisible by 2(even) or not(odd)
-The result is displayed to the user.
"""

#Ask the user for a number
number = int(input("Enter a number: "))

#Check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is even!")

else:
    print(f"{number} is odd!")    
