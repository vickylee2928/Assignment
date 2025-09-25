# main.py

from utils import get_inputs
from logic import perform_operation

def main():
    choice = "y"
    while choice.lower() == "y":
        num1, num2, operation = get_inputs()
        perform_operation(num1, num2, operation)
        choice = input("\nEnter 'y' to continue or any other key to stop: ")

if __name__ == "__main__":
    main()
