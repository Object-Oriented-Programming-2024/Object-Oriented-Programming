from enum import Enum  # Import the module enum
class Major(Enum): # Define a new enumeration class with 2 members CS and IT
     CS = "Computer Science"
     IT = "Information Technology"
class Student: # Create class “Student” with its attributes
     def __init__(self, first_name, last_name, major, date_of_birth):
         self.first_name = first_name
         self.last_name = last_name
         self.major = major
         self.date_of_birth = date_of_birth
# Create student objects
student_1 = Student("Ahmed", "Samir", Major.CS, "02-05-2002")
student_2 = Student("Jennifer", "Jackson", Major.CS, "18-11-2002")
student_3 = Student("John", "Smith", Major.IT, "20-05-2005")
student_4 = Student("Sultan", "Nasser", Major.IT, "21-12-2005")

# Create a list to store the student objects in different techniques to show different methods.
student_list = [student_1] # Add student 1 to the list in one technique
student_list.append(student_2) # Add student_2 to the list in another technique
student_list.insert(2,student_3) # Add student_3 to the list in another technique
student_list.insert(3,student_4) # Add student_4 to the list in another technique

# Accessing student information
for student in student_list:
 print(f"First Name: {student.first_name}")
 print(f"Last Name: {student.last_name}")
 print(f"Major: {student.major.value}")  # Access the Enum value
 print(f"Date of Birth: {student.date_of_birth}")

# Separate students into CS and IT lists using index slicing
cs_list = student_list[:2]  # Students 1 and 2
it_list = student_list[2:]  # Students 3 and 4

# Print CS students
print("CS Students:")
for student in cs_list:
 print(f"First Name: {student.first_name}")
 print(f"Last Name: {student.last_name}")
 print(f"Major: {student.major.value}")  # Access the Enum value
 print(f"Date of Birth: {student.date_of_birth}")

# Print IT students
print("IT Students:")
for student in it_list:
 print(f"First Name: {student.first_name}")
 print(f"Last Name: {student.last_name}")
 print(f"Major: {student.major.value}")  # Access the Enum value
 print(f"Date of Birth: {student.date_of_birth}")

