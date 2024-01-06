colors = {"white", "red", "blue", "green","black"} # Create a set of different Colors
colors.add("yellow") # Add new element to the set using “add”
colors.remove("blue") # Delete an element from the set using “remove”

if "green" in colors: # Use an if statement to check if an element is in the set
 print("Yes, green is in the set.")

print("Colors in the set:")
for color in colors:# Iterate through the elements of the set to print them
 print(color)

dark_colors = {"black", "brown", "maroon"} # Create a new set with different colors

# Create a set that combines all unique elements of the 2 other sets using “union” operation
all_colors = colors.union(dark_colors)

# Create a set containing the common elements of the 2 other sets using “intersection” operation
common_colors = colors.intersection(dark_colors)

# Create a set that give the elements in the “colors” set but not in the “dark_colors” set
non_dark_colors = colors.difference(dark_colors)

# Display the result of the 3 newly formed sets based on the 3 set operations performed
print("All colors:", all_colors)
print("Common colors:", common_colors)
print("Non-dark colors:", non_dark_colors)
