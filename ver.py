"""
ADULT-VERIFICATION PROGRAM
This program continuously asks the user for their age 
and only stops when they provide an age that is above 18

"""

# Program keeps running until user enters an above 18

while True:
    age = int(input("Enter your age: "))
    if age > 18:
        print("You're an adult. Program stopped")
        break
    else:
        print("You're not an adult yet. Try again.")
