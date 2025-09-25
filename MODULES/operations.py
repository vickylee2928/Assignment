# operations.py

def addition(num1, num2):
    sum = num1 + num2
    print(f"This is the sum: {sum}")

def diff(num1, num2):
    difference = num1 - num2
    print(f"This is the difference of the two numbers: {difference}")

def multiply(num1, num2):
    product = num1 * num2
    print(f"This is the product of the two numbers: {product}")

def divide(num1, num2):
    if num2 != 0:
        quotient = num1 / num2
        print(f"This is the quotient of the two numbers: {quotient}")
    else:
        print("Error: Division by zero is not allowed.")
