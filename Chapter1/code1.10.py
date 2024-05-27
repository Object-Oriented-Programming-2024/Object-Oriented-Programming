class Person:
 def __init__(self, name, age):
     self.name = name
     self.age = age

 # The below method shows the string representation of the person.
 def __str__(self):
     return f"{self.name}, {self.age} years old"

 # The below method determines whether two instances are equal when using ‘==’
 def __eq__(self, other):
     return self.name == other.name and self.age == other.age

 # The ‘__lt__’ allows to define a custom ‘<’ comparison between two Person objects.
 def __lt__(self, other):
     return self.name == other.name and self.age == other.age


# Create Person instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Use built-in attributes and methods
print("Class Name:", person1.__class__.__name__)
print("String Representation:", person1)
print("Are they the same age?", person1 == person2)
print("is Alice younger?", person1 < person2)
