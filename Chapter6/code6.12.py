# Import the pickle module
import pickle

# Create a class named “Item”
class Item:
 def __init__(self, category, name, price):
     self.category = category
     self.name = name
     self.price = price

 def __str__(self):
     return f"Category: {self.category} || Name: {self.name} || Price: {self.price}"


# Create 2 instances of the Item Class
item1 = Item(category="Electronics", name="Laptop", price=3260.99)
item2 = Item(category="Electronics", name="SmartPhone", price=2300)

# Use pickle.dump to serialize an object as binary data
file_handler= open('data.dat', 'wb')
pickle.dump(item1, file_handler)

# Use pickle.dumps to serialize an object to a binary string
serialized_data = pickle.dumps(item2)

# Check the type of the object
if isinstance(serialized_data, bytes):
 print("Serialized data is of type bytes")
# Close the file
file_handler.close()
