class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        return f"({self.x}, {self.y})"


# The function below create and return a Point object using the provided coordinates
def create_point(x, y):
    return Point(x, y)


# Create points using the function
point1 = create_point(2, 3)
point2 = create_point(-1, 5)

# Display the coordinates of the points
print("Point 1:", point1.display())
print("Point 2:", point2.display())
