import math
class HealthApp: # Create a class called HealthApp
 def __init__(self):
     self.weight = None
     self.height = None

 def set_weight(self, weight): #This function will ensure weight is a positive number
     try: # Handle the exception when a weight is negative
         if weight <= 0:
             raise ValueError("Weight must be greater than 0.")
         self.weight = weight
     except ValueError as e:
         print(f"Error Occured In:{self.__class__.__name__} Class, Type of Error: {e}")

 def set_height(self, height):
      try: # Handle the exception when a height is negative
         if height <= 0:
             raise ValueError("Height must be greater than 0.")
         self.height = height
      except ValueError as e:
         print(f"Error Occured In:{self.__class__.__name__} Class, Type of Error: {e}")

 def calculate_bmi(self):
     try: # Handle the exception when a weight and height are not provided
         if self.weight is None or self.height is None:
             raise ValueError("Weight and height must be recorded to calculate BMI.")
         return self.weight / math.pow(self.height, 2)
     except ValueError as e:
         print(f"Error Occured In:{self.__class__.__name__} Class, Type of Error: {e}")
         raise e


#Instance of the HealthApp class is created
health_app = HealthApp()
try:
 weight = float(input("Enter your weight (in kg): "))
 health_app.set_weight(weight)

 height = float(input("Enter your height (in meters): "))
 health_app.set_height(height)

 bmi = health_app.calculate_bmi()
 print(f"Your BMI is: {bmi:.2f}")

except ValueError:
     print("Error taking Input")
