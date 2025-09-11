# A Very Simple Student Grade Tracker

# Dictionary to store student names as keys and their grades as values
students = {}

# Function to add a new student
def add_student(name):
    if name not in students:
        students[name] = []
        print(f"Student {name} added successfully.")
    else:
        print(f"Student {name} already exists.")

# Function to add a grade for an existing student
def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f"Grade {grade} added for {name}.")
    else:
        print(f"Student {name} not found.")

# Function to calculate average grade for each student
def average_grade(name):
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    else:
        return None

# Function to find the student with the highest average
def top_student():
    if not students:
        return None
    averages = {name: average_grade(name) for name in students if students[name]}
    if not averages:
        return None
    return max(averages, key=averages.get)

# Function to display all students and their grades in a formatted table
def display_students():
    print("\n--- Student Grade Tracker ---")
    print("{:<15} {:<20} {:<10}".format("Name", "Grades", "Average"))
    print("-" * 45)
    for name, grades in students.items():
        avg = average_grade(name)
        avg_display = f"{avg:.2f}" if avg is not None else "N/A"
        print("{:<15} {:<20} {:<10}".format(name, str(grades), avg_display))
    print("-" * 45)


# ---------------- Example Usage ----------------

add_student("Alice")
add_student("Bob")
add_grade("Alice", 85)
add_grade("Alice", 90)
add_grade("Bob", 70)
add_grade("Bob", 75)

display_students()

print("\nTop Student:", top_student())