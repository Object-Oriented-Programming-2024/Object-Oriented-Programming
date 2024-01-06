# Set age limit for a job application
try:
 age = int(input("Enter your age: "))
 assert (age > 20 and age < 60), age
 print("You can apply for the job!")
except AssertionError as ex:
 print("Age", ex, "is not suitable for this job.")
except:
 print("Something went wrong.")
