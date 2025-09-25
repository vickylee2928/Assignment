# utils.py

def get_inputs():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, / or sum, difference, product, quotient): ").lower()
    return num1, num2, operation
