class Student:
 def __init__(self, stud_ID, stud_first_name, stud_last_name, stud_password):
     self.__stud_ID = stud_ID
     self.__stud_first_name = stud_first_name
     self.__stud_last_name = stud_last_name
     self.__stud_password = stud_password

 def get_stud_ID(self):
     return self.__stud_ID

 def __provide_permission(self, password):
     return password == self.__stud_password

 # The set and get methods for students' first and last names are defined
 def set_stud_first_name(self, stud_first_name, password):
     if self.__provide_permission(password):
         self.__stud_first_name = stud_first_name

 def set_stud_last_name(self, stud_last_name, password):
     if self.__provide_permission(password):
         self.__stud_last_name = stud_last_name

 def get_stud_first_name(self):
     return self.__stud_first_name

 def get_stud_last_name(self):
     return self.__stud_last_name


# Create a Student instance
stud_1 = Student(stud_ID="S000123", stud_first_name="John",
              stud_last_name="Davis", stud_password="John123")

# Access and print the first name using the get_stud_first_name method
print("First Name: ", stud_1.get_stud_first_name())

# Use set_stud_first_name to attempt changing the first name with the correct password
stud_1.set_stud_first_name("Jonathan", "John123")

# Print the updated first name using get_stud_first_name
print("First Name: ", stud_1.get_stud_first_name())
