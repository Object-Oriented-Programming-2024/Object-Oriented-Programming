class Vehicle:
     """Class to represent any vehicle"""
  
     # Define the attributes
     def __init__(self, manufacturer="", num_doors=0, fuel_capacity=0.0):
         self.manufacturer = manufacturer
         self.num_doors = num_doors
         self.fuel_capacity = fuel_capacity
 
 
 # Create objects of class Vehicle
james_car = Vehicle()
her_car = Vehicle("Ford", 5, 65.5)