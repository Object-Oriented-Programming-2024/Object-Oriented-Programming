class Room: # Class to represent individual rooms
 def __init__(self, name):
     self.name = name # Initialize room name


class Apartment: # Class to represent an apartment consisting of multiple rooms
 def __init__(self):
     self.rooms = [] # A list to store rooms
     for i in range(5): # Create 5 rooms and add them to the list
         self.rooms.append(Room(f"Room {i + 1}"))

 def list_rooms(self): # display all rooms in the apartment
     for room in self.rooms:
         print(f"Room Name: {room.name}")


# Example of using these classes
my_apartment = Apartment()
my_apartment.list_rooms()
