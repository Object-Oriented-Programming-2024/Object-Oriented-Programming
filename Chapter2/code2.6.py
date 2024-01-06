class Customer: # Create a class customer with its attributes
 def __init__(self, first_name, last_name, email, transactions):
     self.first_name = first_name
     self.last_name = last_name
     self.email = email
     self.transactions = transactions


# Create two customer Objects “customer 1” and “customer 2”
customer_1 = Customer("David", "Walker", "dwalker@gmail.com",
  [("T10123", "12-10-2023 8:00:00", "Starbucks Coffee Pods", 25),
  ("T10125", "12-10-2023 8:02:00", "Cucumbers", 10.50),
   ("T10131", "13-10-2023 8:02:00", "Water bottle 1 L", 2.50)])

customer_2 = Customer("Emily", "Mitchel", "emitchel@xyz.com",
 [("T10140", "20-11-2023 10:00:00", "Oreo Cookies", 15.0),
 ("T10141", "121-11-2023 11:02:00", "Chicken 1 pound", 50.50),
 ("T10145", "25-11-2023 12:02:00", "Pepsi Can", 3.50)])

# Create a dictionary called “customers”
customers_dictionary = {
 "C0001": customer_1,
 "C0002": customer_2
}

customer_id = "C0001" # A customer ID is selected
if customer_id in customers_dictionary: # Check if this customer is in the dictionary
 selected_customer = customers_dictionary[customer_id] # Retrieve selected student’ object

 # Print the selected customer’s details
 print("Customer ID:", customer_id)
 print("First Name:", selected_customer.first_name)
 print("Last Name:", selected_customer.last_name)
 print("Email:", selected_customer.email)
 print("Transactions:")

 # Iterate into the transaction to print its details.
 for transaction in selected_customer.transactions:
     print("  Transaction ID:", transaction[0])
     print("  Transaction Date and Time:", transaction[1])
     print("  Transaction Description:", transaction[2])
     print("  Transaction Amount:", transaction[3])
     print()

else: # If the customer is not in the dictionary, print the below message
 print("Customer not found.")
