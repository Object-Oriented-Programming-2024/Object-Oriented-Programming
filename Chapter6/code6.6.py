#A basic user class for illustration
class User:
 def __init__(self,fullname,address,phone_number):
     self.fullname=fullname
     self.address=address
     self.phone_number=phone_number
 def __str__(self):
     return f"{self.fullname},{self.address},{self.phone_number}\n"


# Appending users to an existing csv file
csvfile = open("users.csv", 'r')

#Creating a list with each row of the file as a list item
userList=csvfile.readlines()
#lopping through the list of rows
for info in userList:
 #spliting the row based on comma
 fullname,address,phone_number=info.split(",")
 #Creating the User instance
 user=User(fullname.strip(),address.strip(),phone_number.strip())
 print(user.__str__())
