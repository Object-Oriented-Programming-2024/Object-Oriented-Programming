from enum import Enum # Import the module enum

class Student: # Create class “Student” with its attributes
 def __init__(self, first_name, last_name, major, date_of_birth):
     self.first_name = first_name
     self.last_name = last_name
     self.major = major
     self.date_of_birth = date_of_birth

class Major(Enum): # Define a new enumeration class with 3 members CS, IT and EE
 CS = "Computer Science"
 IT = "Information Technology"
 EE = "Electrical Engineering"

# Create a list of student IDs and a list of first names
student_ids = ["S0123789", "S0123790", "S0123821"]
first_names = ["John", "Adam", "Ann"]

# Create a dictionary using zip
student_names = dict(zip(student_ids, first_names))

# Create “student_info” dictionary with IDs as Keys and corresponding student Object as values
student_info = {
 "S0123789": Student("Ahmed", "Samir", Major.CS, "02-05-2002"),
 "S0123790": Student("Jennifer", "Jackson", Major.IT, "18-11-2002")
}

# Add new element to both dictionaries.
student_names["S0123822"] = "Mike Johnson"
student_info["S0123822"] = Student("Michael", "Johnson", Major.CS, "10-03-2001")

# Change the values of a specific key “student ID” in both dictionaries.
student_names["S0123789"] = "Ahmed Samir"

# Update with the use of “update” to change the major for the specific student
student_info.update({"S0123789": Student("Ahmed", "Samir", Major.EE, "02-05-2002")})

# Delete one element for both dictionaries for a specific key “student ID”
del student_names["S0123790"]
del student_info["S0123790"]

# Display the amended dictionaries
print("Student Names:")
for student_id, name in student_names.items():
 print(f"{student_id}: {name}")

print("\nStudent Information:")
for student_id, student in student_info.items():
 print( f"{student_id}: {student.first_name } {student.last_name} ({student.major.value}),"\
       f"DOB: {student.date_of_birth}")

# Display the keys of the student_info dictionary
print("Student IDs:")
for student_id in student_info.keys():
 print(student_id)
