import xml.etree.ElementTree as ET

class Person: # Create Person Object
 def __init__(self, name, gender):
     self.name = name
     self.gender = gender
     self.children = []


# Parse the XML file
tree = ET.parse('familytree.xml')
root = tree.getroot()

# A Function to create a Person from ElementTree node
def create_person_from_element(person_element):
 person = Person(person_element.attrib['name'], person_element.attrib['gender'])
 for child_element in person_element:
     child_person = create_person_from_element(child_element)
     person.children.append(child_person)
 return person


# A Function to print the family tree recursively
def print_family_tree(person, level):
 print(".." * level + f"{person.name} ({person.gender})")

 # Print recursively the information for each child
 for child in person.children:
     print_family_tree(child, level + 1)

# Create a Person object representing the entire family tree
person_tree_root = create_person_from_element(root[0])

# Print the family tree starting from the root Person object
print_family_tree(person_tree_root, 0)
