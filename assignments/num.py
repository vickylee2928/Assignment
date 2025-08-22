"""
NUMBER GUESSING GAME 

This program implements a single number guessing where the player must guess the secret number 
"""

secret_number = 7
guess = None

while guess != secret_number:
    try:
      guess = int(input("Guess the number: "))
      if guess == secret_number:
        print("Correct! You win.")
      else:
        print("Wrong guess. Try again!")
    except ValueError:
       print("Please enter a valid number")    
