"""
YES/NO PROGRAM
This program asks the user if they want to continue or not
"""

print("CONTINUATION PROGRAM")
print("Do you want to continue? (y/n): ")


while True:
    choice = input("Enter your choice (y/n): ").lower()
    if choice == "y":
        print("Continuing....")
        print("Doing some work...")
        print("Ready for next choice")

    elif choice == "n":
        print("Stopping program")
        print("Goodbye")
        break
    else:
        print("Invalid choice! Please enter either 'y' for yes or 'n' for no.")