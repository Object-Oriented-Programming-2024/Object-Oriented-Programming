import json5 as json

# Define a class named Item with attributes category, name and price
class Item:
 def __init__(self, category, name, price):
     self.category = category
     self.name = name
     self.price = price

 def __str__(self):
     return f"Category: {self.category} || Name: {self.name} || Price: {self.price}"


# Create a custom decoder class for Item objects
class ItemDecoder:
 def __init__(self):
    self.item_list=[]

 def decode(self, jsonItem):
     if "category" in jsonItem and "name" in jsonItem and "price" in jsonItem:
         item=Item(jsonItem["category"], jsonItem["name"], jsonItem["price"])
         return self.item_list.append(item)
     return jsonItem


# Open the JSON file in binary read mode
jsonData = open("items.json", "rb")

# Create an instance of the custom decoder class
item_decoder = ItemDecoder()

# Decode JSON data using json.load with the custom decoder
json.load(jsonData, object_hook=item_decoder.decode)

# Print the Item objects
for item in item_decoder.item_list:
 print(item)
