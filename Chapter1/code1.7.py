import math

class Circle:
 def __init__(self, radius):
     self.radius = radius

 # The below public method will calculate the area of the circle
 def calculate_area(self):
     return math.pi * self.radius ** 2


# Create a Circle instance
circle1 = Circle(5)

# Calculate and print the area and circumference
print("Circle Radius:", circle1.radius)
print("Circle Area:", circle1.calculate_area())
