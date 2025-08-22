"""
POSITIVE NUMBER COLLECTOR
This program continuously asks the user for integer inputs
and collects them until a neagative number is entered
"""



print("POSITIVE-NUMBERS COLLECTOR")
print("Enter positive numbers only!!")


while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("You entered a negative number. Program stopped.")
        break
    else:
        print(f"You entered: {num}")
