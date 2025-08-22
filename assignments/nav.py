"""
APTECH TO ABAKPA/EMENE DIRECTION GUIDE

This program assists a user in navigating from Aptech to either Abakpa or Emene
It asks for the user's name and destination choice, then provides step-by-step directions

Developed by: Clara
"""

#Get user's name and direction
user_name = input("Hello! What's your name? " )
print(f"Welcome, {user_name}. You're currently at Aptech.")

#Asks for destination
print("Where would you like to go?: ")
print("1. Abakpa")
print("2. Emene")
choice = input("Enter your choice(1 or 2): ")

#Provide directions based on choice
if choice == "1":
    print("Directions from Aptech to Abakpa:")
    print("-Walk to the nearby bus stop at Holy Ghost Park")
    print("-Take a bus or keke(tricycle) heading towards Abakpa")
    print("-Stop at Abakpa Junction or your specific destination")
    print("-Safe journey!")

elif choice == "2":
    print("Directions from Aptech to Emene:")
    print("-Walk to the main road and board a bus or keke going towards Emene ")
    print("-The bus will pass through New Haven and then proceed to Emene")
    print("-Alight at your preferred stop in Emene(e.g., Timber Market.)")
    print("-Safe journey")

else:
    print("Invalid choice. Please enter 1(Abakpa) or 2(Emene)" )    
