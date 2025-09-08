"""
ATM Simulator 
This program simultes a simple ATM machine:
1. Starts with a balance of $1000
2. Let's the user check balance, deposit or withdraw.
"""

balance = 1000 #starting balance

#Show the ATM menu
print("ATM Menu:")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

#Ask user for their choice 
choice = int(input("Choose an option: "))

if choice ==1:
    #option 1: Show balance
    print(f"Your balance is: ${balance}")

elif choice ==2:
    #option 2: Deposit money
    amount =int(input("Enter deposit amount: $"))
    balance += amount
    print(f"You deposited ${amount}. Your new balance is ${balance}")

elif choice == 3:
    #option 3: Withdraw money
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print(f"Transaction successful! New balance: ${balance}")
    else:
        print("Insufficient funds!")

else:
    print("Invalid option.")