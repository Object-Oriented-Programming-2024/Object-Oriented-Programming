# Set age limit for a job application
try:
 age = int(input("Enter your age: ")) # Get age
 assert (age > 20 and age < 60), age  # Check if age is between 20 and 60
 print("You can apply for the job!")
except AssertionError as ex: # Catches the error raised if the age is not between 20 and 60
 print("Age", ex, "is not suitable for this job.")
except: # Catches all errors
 print("Something went wrong.")
