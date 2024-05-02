class Polygon: # Class to represent a Polygon
 def __init__(self, sides=None):
     if sides is None:
         sides = []
     self.sides=sides
 def calculate_area(self, *args):
     if len(args) == 0:
         print("Number of sides for the polygon are not provided.")
     elif len(args) == 3:
         # A triangle with 3 sides a, b, and c
         self.sides = args
         a,b,c=self.sides
         #Calculating Area of a triangle using parameter
         s = (a + b + c) / 2
         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
         print(f"Area of the Triangle: {area}")
     elif len(args) == 4:
         # A quadrilateral with 4 sides a, b, c, and d
         self.sides = args
         a, b, c, d = self.sides
         # Calculating area for a general quadrilateral based on parameter
         s = (a + b + c + d) / 2
         area = (s - a) * (s - b) * (s - c) * (s - d)
         print(f"Area of the Quadrilateral: {area}")
     else:
         print("Unsupported number of sides for calculation.")


# Examples of method overloading with and without parameters
polygon1 = Polygon()
polygon2 = Polygon([5,6,2,3])

# Examples of method overloading with arguments of variable length
polygon1.calculate_area()            # Calculate the area if sides are not given.
polygon1.calculate_area(3, 4, 5)      # Calculate the area for a triangle
polygon1.calculate_area(1, 2, 3, 4)   # Calculate the area for a quadrilateral
