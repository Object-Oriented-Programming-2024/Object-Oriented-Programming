import xml.dom.minidom

class Visitor: # Create a Visitor class
 def __init__(self, name, age, rides):
     self.name = name
     self.age = age
     self.rides = rides

 def __str__(self):
     return f"Visitor Info: name={self.name}, age={self.age}, rides taken={self.rides}"


#Parse the xml document and store the tree structure in a variable
dom = xml.dom.minidom.parse("amusement_park.xml")

# Get the root element of the XML document
amusement_park = dom.documentElement

# Find all nodes with the visitor tags in the XML document
visitor_nodes = amusement_park.getElementsByTagName("visitor")

# Create a list to store Visitor objects
visitors_list = []

# Iterate over each visitor node
for each_visitor_node in visitor_nodes:
 # Find a node called "name" within each_visitor_node & access the first occurrence
 name_node=each_visitor_node.getElementsByTagName("name")[0]
 # Find the first childNode to get the text entered within the name node
 name =name_node.childNodes[0].data
 age_node = each_visitor_node.getElementsByTagName("age")[0]
 age=int(age_node.childNodes[0].data)

 # Find the list of rides taken by the visitor
 rides_node = each_visitor_node.getElementsByTagName("rides")[0]
 # Find all the nodes starting with the tag "rides", a list will be returned
 ride_nodes = rides_node.getElementsByTagName("ride")
 rides = []
 for ride in ride_nodes:
     rides.append(ride.childNodes[0].data )

 # Create a Visitor object and add it to the list
 visitor = Visitor(name, age, rides)
 visitors_list.append(visitor)

for visitor in visitors_list:
 print(visitor)
