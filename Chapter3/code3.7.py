import math
x=-1.7
y=0.3
try:
 # Use the built-in power function
 result=math.pow(x,y)
 print(result)
#This except clause will catch if a decimal value is entered as an exponent
except ValueError as ve:
 print("The exponent can not be a decimal value")
