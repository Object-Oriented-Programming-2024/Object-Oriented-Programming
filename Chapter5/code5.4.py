class Wheel: # Class that represents individual wheels
 def __init__(self, position):
     self.position = position # Initialize wheel position


class Sedan: # Class that represents a Sedan Car with 4 wheels
 def __init__(self, wheels):
     if len(wheels) != 4: # Check if the Sedan has exactly 4 wheels
         raise ValueError("A sedan must have exactly four wheels.")
     self.wheels = wheels

 def list_wheels(self): # Display the position of each wheel in the Sedan
     for wheel in self.wheels:
         print(f"Wheel Position: {wheel.position}")


# Example of using these classes
wheels = [Wheel("Front Left"), Wheel("Front Right"),
       Wheel("Rear Left"), Wheel("Rear Right")]
my_sedan = Sedan(wheels)
my_sedan.list_wheels()
