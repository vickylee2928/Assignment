"""
PASSWORD STRENTH CHECKER
This program checks if a password is strong by verifying:
-  At least 8 characters long
- Contains one uppercase
- Contains onr lowercase
- Contains numbers
It keeps asking until a strong password is entered
"""
#Control the loop
strong_password = False

print("Create a strong password")
print("Must be 8+ characters with uppercase, lowercase, and numbers.")
#Keeps asking until we get a strong password
while not strong_password:
    password = input("Enter your password: ")
#Check length first
    if len(password) < 8:
        print("Too short! Need at least 8 characters")
        continue # Go back to the start of the loop

#Check for different character types
    has_upper = False
    has_lower = False
    has_digit = False
#Check each character in password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True


#Checks if all the requirements are met
    if has_upper and has_lower and has_digit:
        strong_password = True
        print("Great! Your password is strong.")
    else:
        if not has_upper:
            print("Need at least one UPPERCASE letter")

        if not has_lower:
            print("Need at least one lowercase letter")

        if not has_digit:
            print("Need at least one number")
        print("Please try again.")