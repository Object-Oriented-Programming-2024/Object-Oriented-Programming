from enum import Enum

class Color(Enum):
    """An enumerator type class that defines colors"""
    WHITE = 1
    BLACK = 2
    RED = 3


class Vehicle:
    """Class to represent any vehicle"""

# Define the attributes
def __init__(self):
    self.manufacturer = ""
    self.model = ""
    self.num_doors = 0
    self.color = Color()
    self.fuel_capacity = 0.0
    self.current_speed = 0.0  #Initialize a speed property with a default value of 0

# Find below the behaviors of the object	
def turn_left(self):
    pass

def turn_right(self):
    pass

def stop_car(self):
    pass

def accelerate(self):
    pass

# The methods below represent the Setter and Getter functions

def get_manufacturer(self):
    pass

def get_number_of_doors(self):
    pass

def get_engine_state(self):
    pass

def set_engine_state(self):
    pass

def set_current_speed(self):
    pass

def set_color(self):
    pass


# Create an object of class Vehicle
james_car = Vehicle()
