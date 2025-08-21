"""
Simple calculator program
User choose an operation
and the program performs it on two numbers
"""

#Simple Calculator With User-Chosen Operation

#Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Ask the user which operation they want to perform
operation = input("Choose an operation(sum, difference, product, quotient): ")


#Perform the chosen operation using conditional statements

if operation.lower() =="sum":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operation.lower()  == "difference":
    result = num1 + num2
    print(f"Result: {num1} - {num2} = {result}")

elif operation.lower()  == "product":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operation.lower()  == "quotient":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    

else:
 print("Invalid operation! Please choose from sum, difference, product, quotient")    