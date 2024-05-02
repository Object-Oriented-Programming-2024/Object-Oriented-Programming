class Server: #Server lass definition
 _server = None # Class variable to store the single instance

 def __new__(cls):
     if cls._server is None: # Skip this method if _server is not None
         # Create a new instance only once in the program using the __new__ method
         cls._server = super(Server, cls).__new__(cls)
     return cls._server

# Create two isntances of the Server Class
server1 = Server()
server2 = Server()
# Both server1 and server2 refer to the same instance
print("Are they the same instance?", server1 is server2)
