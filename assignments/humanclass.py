"""
This program defines a Human class in Python.
It shows how to create a class with attributes (properties) and methods (actions).
Then it creates an object (person) and demonstrates how to use it.
"""

class Human:

    # The Human class is a blueprint for creating human objects.
    # It contains attributes (eyes, hair_color, legs, gender, height)
    # and methods (walking, speaking, breathing).
    

    def __init__(self, eyes, hair_color, legs, gender, height):
        
       # __init__ is the constructor method.
       # It runs automatically when you create a new Human object.
       # Parameters:
       #   - eyes: number of eyes
       #   - hair_color: color of the hair
       #   - legs: number of legs
       #   - gender: male or female
       #   - height: height of the human
       # self is used to store these values in the object.
        
        self.eyes = eyes
        self.hair_color = hair_color
        self.legs = legs
        self.gender = gender
        self.height = height

    def walking(self): #This method prints a message to show the human is walking.
        print("I am walking")

    def speaking(self):#This method prints a message to show the human is talking.
        print("I am talking")

    def breathing(self):#This method prints a message to show the human is breathing.
        print("I am breathing")


# ---------------- Example usage ----------------

"""
Here we create an object 'person' from the Human class.
We pass values for eyes, hair_color, legs, gender, and height.
"""
person = Human(2, "black", 2, "female", "5.6ft")

"""
These print statements display the attributes of the person object.
We use dot notation (person.attribute_name) to access them.
"""
print("Eyes:", person.eyes)           # Prints number of eyes
print("Hair Color:", person.hair_color) # Prints hair color
print("Legs:", person.legs)             # Prints number of legs
print("Gender:", person.gender)         # Prints gender
print("Height:", person.height)         # Prints height

"""
Here we call the methods of the Human class using the object.
Each method prints a message when called.
"""
person.walking()   # Prints "I am walking"
person.speaking()  # Prints "I am talking"
person.breathing() # Prints "I am breathing"