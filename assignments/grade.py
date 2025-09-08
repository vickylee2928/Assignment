"""
Grade Calculator Program
This progarm asks the user for a score(0-100), checks validity,
assigns a letter grade(A-F), and prints an encouraging message 

Developed by: Clari
"""

#Ask user for score
score = int(input("Enter your score(0-100): "))

#Checks if score is valid
if score < 0 or score > 100 :
    print("Invalid input! Score must be within the range 0-100.")

#Assign grade
if score >= 90:
    grade = "A"
    message = "Excellent Work!"


elif score >= 80:
    grade = "B"
    message = "Great job, keep pushing."


elif score >= 70:
    grade = "C"
    message = "Good effort, you can do even better."


elif score >= 60:
    grade = "D"
    message = "Don't give up, keep trying."


else:
    grade = "F"
    message = "Keep working hard, you'll improve!"

    
#output result 
print(f"Your grade is: {grade}")
print(message)

