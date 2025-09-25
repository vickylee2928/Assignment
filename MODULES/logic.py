# logic.py

from operations import addition, diff, multiply, divide

def perform_operation(num1, num2, operation):
    if operation == "+" or operation == "sum":
        addition(num1, num2)
    elif operation == "-" or operation == "difference":
        diff(num1, num2)
    elif operation == "*" or operation == "product":
        multiply(num1, num2)
    elif operation == "/" or operation == "quotient":
        divide(num1, num2)
    else:
        print("Invalid operation! Please choose from +, -, *, / or sum, difference, product, quotient.")
