#A simple user class for illustration
class User:
 def __init__(self,fullname,address,phone_number):
     self.fullname=fullname
     self.address=address
     self.phone_number=phone_number
 def __str__(self):
     return f"{self.fullname},{self.address},{self.phone_number}\n"


#Create three Users
user1 = User("Ismail Alhamidi", "123 Main St CityA", "555-1234")
user2 = User("Foster Smith", "456 Oak St CityB", "555-5678")
user3 = User("Stephani Johnson", "789 Pine St CityC", "555-9101")

#List of users of the application
userList=[user1.__str__(),user2.__str__(),user3.__str__()]
# Appending users to an existing csv file
csvfile = open("users.csv", 'a')
#Writing a list of users to the file
csvfile.writelines(userList)
