"""
This program is a simple password checker.
it asks the user to enter a password
-If the password is "Mr Frank", it prints "Access given"
-If not, it prints "Access denied"
"""

#Simple Password Checker
password = input("Enter password: ")

if password == "MR FRANK":
    print("Access granted")
else:
    print("Access denied")    