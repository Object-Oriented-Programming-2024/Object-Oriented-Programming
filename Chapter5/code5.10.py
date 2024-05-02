class User: # Define a User class to represent a generic user
 def __init__(self, username, password): # Initialize user attributes
     self.username = username
     self.password = password
     self.account_info=None #User account info, initially set to None

 def __str__(self):
     return (
    f"Username: {self.username} || "
    f"Password={self.password} || "
    f"Account Details: {self.account_info}")


class Subscriber(User): # Define Subscriber class inherited from User Class
 def set_info(self): # Subscriber overrides set_info to customize the account info
     self.account_info= "Subscriber: Regular user with viewing access."


class PremiumUser(User): # Define Premium User class inherited from User Class
 def set_info(self): # Premium User overrides set_info to customize the account info
     self.account_info= "PremiumUser: User with subscription for premium content."


class Administrator(User): # Define Administrator class inherited from User Class
 def set_info(self): # Administrator overrides set_info to customize the account info
     self.account_info= "Administrator: User with administrative privileges."


class UserFactory: # Userfactory class creates user based on their type
 @staticmethod
 def create_user(user_type, username, password):
     user=None
     if user_type == "subscriber":
         user= Subscriber(username, password)
     elif user_type == "premium":
         user= PremiumUser(username, password)
     elif user_type == "administrator":
         user = Administrator(username, password)
     else:
         raise ValueError("Invalid user type")
     user.set_info()# Set additional information for the created user
     return user


# Utilizing Userfactory  for Initializing Users
user1 = UserFactory.create_user("subscriber", "Hassan Saeed", "165Dst31")
user2 = UserFactory.create_user("premium", "Mariam Khalil", "#29Bev50")
user3 = UserFactory.create_user("administrator", "Gulbano Ali", "3h!80dem6")
print(user1)
print(user2)
print(user3)
