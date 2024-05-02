class Customer:
 def __init__(self,id,fname,lname):
     self.__customerID=id
     self._firstName=fname
     self._lastName=lname
     self.requests = []  # A list to store requests made by the customer

 # Getters and setters for the class have been removed to reduce the length of the code

 # Method to add a request placed by the customer
 def place_request(self, request):
     self.requests.append(request)
 # Method to return all requests added to the customer class
 def get_requests(self):
     return self.requests


class Request:
 def __init__(self, r_id, r_date, r_status, r_subject, r_description):
     self.__requestID = r_id
     self.__requestDate = r_date
     self.__requestStatus = r_status
     self.__requestSubject = r_subject
     self.__requestDescription = r_description

 def display_info(self):
      print(f"Request ID: {self.__requestID}|| Request Date: {self.__requestDate}" 
            f"|| Status: {self.__requestStatus}|| Subject: {self.__requestSubject}"
            f"|| Description: {self.__requestDescription}")


# Creating a Custmer Object
customer1 = Customer(1, "Ismail", "khalifa")
# Creating two Request objects
request1 = Request(101,"2023-06-24","Open","Technical Support",
                "Having trouble with my computer")
request2 = Request(102,"2023-06-25","Open","Return/Exchange",
                "Does not meet the required specifications")

# Adding requests to the customer
customer1.place_request(request1)
customer1.place_request(request2)
print(f"Requests placed by the customer:")
for request in customer1.get_requests():
 request.display_info()
