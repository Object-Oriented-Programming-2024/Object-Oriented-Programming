# Create a function to square a negative number
def squareNeg(val):
 assert val < 0 # Raise an AssertionError if the value is positive
 return val ** 2

try:
 # Input: Get a user input
 negativenumber = int(input("Enter a negative number: "))
 # Call function to square the negative number
 result = squareNeg(negativenumber)
except AssertionError:
 print("We need a negative value.")
except:
 print("Something went wrong.")
else:
 print(result, "is the square of your number")
finally:
 print("Bye")
