# Import xml.sax module for XML parsing
import xml.sax

# Define a class representing an item in the menu
class Item:
 def __init__(self, category, name, price):
     self.category = category
     self.name = name
     self.price = price
 def __str__(self):
         return f"Category: {self.category} || Name: {self.name} || Price: {self.price}"


# Define a content handler for parsing XML
class MenuHandler(xml.sax.ContentHandler):
 def __init__(self):
     self.menu_items = []
     self.current_item = None
     self.buffer = ""

 # Sets up MenuHandler for a new XML element, creating Item and resetting buffer
 def startElement(self, name, attrs):
     if name == "item":
         self.current_item = Item("", "", "")
     self.buffer = ""

 # Handles the closure of XML elements, updating Item attributes.
 def endElement(self, name):
     if name == "category":
         self.current_item.category = self.buffer
     elif name == "name":
         self.current_item.name = self.buffer
     elif name == "price":
         self.current_item.price = self.buffer
     elif name == "item":
         self.menu_items.append(self.current_item)

 # Accumulate the character data in the buffer
 def characters(self, content):
     self.buffer += content.strip()


# Create an instance of MenuHandler
handler = MenuHandler()
# Parse the XML file "Menu.xml” using the handler
xml.sax.parse("Menu.xml",handler)

# Print the menu details
for item in handler.menu_items:
  print(item)
