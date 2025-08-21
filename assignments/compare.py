"""
This program compare two numbers given by the user.
it prints out the greater number.
-if the first is bigger, it prints that one.
-if the second is bigger, it prints that one
-if they are equal, it says both are equal. 
"""

#Program to find the greater of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("The greater number is:" ,num1)
elif num2 > num1:
    print("The greater number is:" ,num2)

else:
    print("Both numbers are equal.")        