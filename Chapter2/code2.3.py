new_york_coordinates=(-74.0060,40.7128) # Create a tuple of New York city coordinates
# Print the New York city coordinate tuple using indexing
print("New York Coordinates: ","Lat:",new_york_coordinates[0],new_york_coordinates[1])
# Create a list of tuples for different cities and their corresponding coordinates.
city_coordinates_list = [
 ("New York", (40.7128, -74.0060)),
 ("Los Angeles", (34.0522, -118.2437)),
 ("Chicago", (41.8781, -87.6298)),
 ("San Francisco", (37.7749, -122.4194)),
 ("Miami", (25.7617, -80.1918)),
 ("Abu Dhabi", (24.4667, 54.3667))
]
# Iterate through the list of tuples to extract the city name and coordinates from each tuple
for city_coordinates in city_coordinates_list:
 city=city_coordinates[0]
 coordinates=city_coordinates[1]
 lat=coordinates[0]
 lng=coordinates[1]
 print("City:",city," Lat:",lat," Lng:",lng) # Print the city name with its coordinates

#How to change elements in an immutable tuple
new_york_list=list(new_york_coordinates) # Convert tuple to list
new_york_list[0], new_york_list[1]= new_york_list[1], new_york_list[0] # Swap the elements
new_york_coordinates = tuple(new_york_list) # convert back to tuple
