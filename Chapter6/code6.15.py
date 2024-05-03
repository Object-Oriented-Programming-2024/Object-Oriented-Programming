# Import the json5 library as json
import json5 as json

# Define a class named Item with attributes category, name and price
class Item:
 def __init__(self, category, name, price):
     self.category = category
     self.name = name
     self.price = price

 def __str__(self):
     return f"Category: {self.category} || Name: {self.name} || Price: {self.price}"


# Create instances of the Item class
item1 = Item(category="Electronics", name="Laptop", price=3260.99)
item2 = Item(category="Electronics", name="SmartPhone", price=2300)

file_handler= open('data.json', 'w')
# Serialize to JSON and write to a file using json.dump
json.dump(item1.__dict__, file_handler)
file_handler.close()

# Serialize to JSON variable using json.dumps
json_variable = json.dumps(item2.__dict__)

# Deserialize JSON  from file using json.load
file_handler= open('data.json', 'r')
file_item = json.load(file_handler)

# Deserialize JSON variable using json.loads
memory_item = json.loads(json_variable)

# Create new instances from the deserialized data
deserialized_item1 = Item(**file_item)
deserialized_item2 = Item(**memory_item)

# Print the deserialized items
print("\nItem1 deserialized from file:")
print(deserialized_item1)

print("\nItem2 deserialized from a variable:")
print(deserialized_item2)
