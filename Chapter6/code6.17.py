import datetime
from enum import Enum
import pickle
import json5 as json
import datetime


class TransactionType(Enum):
 """An enumerator type class that defines the types of transactions"""
 INCOME = 1  # an income type defines a transaction of a gained amount of money
 EXPENSE = 2  # an expense type defines a transaction of a spent amount of money


class Currency(Enum):
 """An enumerator type class that defines the types of currencies"""
 USD = 1  # US Dollars
 EUR = 2  # Euro
 GBP = 3  # Great Britain Pound
 AED = 4  # Arab Emirati Dirham


class Transaction:
 """A class that represents a financial transaction"""
 # a static variable that keeps track of the number of transactions
 transaction_count = 0

 # Initialize the Transaction class
 def __init__(self, transaction_type, amount, currency, description, date_time):
     # Increment the number of transactions with the creation of a new transaction
     Transaction.transaction_count += 1

     # Assign a unique transaction ID based on the number of transactions
     self.__trans_id = "T" + str(Transaction.transaction_count)
     self.__trans_type = transaction_type
     self.__trans_amount = amount
     self.__trans_description = description
     self.__trans_currency = currency
     self.__trans_date_time = date_time

 def get_trans_id(self):
     return self.__trans_id

 def get_transaction_type(self):
     return self.__trans_type

 def get_trans_amount(self):
     return self.__trans_amount

 def get_trans_date_time(self):
     return self.__trans_date_time

 def get_trans_currency(self):
     return self.__trans_currency

 def get_trans_description(self):
     return self.__trans_description

 def set_trans_description(self, description):
     self.__trans_description = description

 def to_dict(self):
        return {
            "__trans_id": self.__trans_id,
            "__trans_type": self.__trans_type.name,  # Convert Enum to string
            "__trans_amount": self.__trans_amount,
            "__trans_description": self.__trans_description,
            "__trans_currency": self.__trans_currency.name,  # Convert Enum to string
            "__trans_date_time": self.__trans_date_time.strftime("%Y-%m-%d %H:%M:%S")  # Convert datetime to string
        }


 # Define a string representation of the transaction
 def __str__(self):
     return (
         'Transaction ID: {id}, Amount: {amount} {currency}, '
         'Type: ({type}), Description: {description}, '
         'Date & Time: {date_time}'.format(
             id=self.__trans_id,
             amount=self.__trans_amount,
             currency=Currency(self.__trans_currency).name,
             type=TransactionType(self.__trans_type).name,
             description=self.__trans_description,
             date_time=self.__trans_date_time))


class TransactionManager:
 """
     This class keeps track of transactions and allows users
     to create transactions, and calculate their total amount
 """

 def __init__(self):
     # Transactions managed by TransactionManager as a list
     self.__transactions = []

 # A function that allows the creation of a transaction
 # User Input is collected for each transaction
 def create_transaction(self):
     # Transaction type
     trans_type_input = input("Transaction type (Expense/Income)? ")
     assert trans_type_input in ["Expense", "Income"], "Invalid Input"
     trans_type = TransactionType.EXPENSE  # Defaulting the type to Expense
     if trans_type_input == "Income":
         trans_type = TransactionType.INCOME
     trans_amount = float(input("Transaction amount? "))
     if trans_type == TransactionType.EXPENSE:
         trans_amount *= -1

     # Transaction description
     trans_description = input("Transaction description: ")

     # Transaction currency
     trans_currency_input = input("Currency of Transaction (USD/EUR/GBP/AED)? ")
     assert trans_currency_input in ["USD", "EUR", "GBP", "AED"], "Invalid Input"
     if trans_currency_input == "USD":
         trans_currency = Currency.USD
     elif trans_currency_input == "EUR":
         trans_currency = Currency.EUR
     elif trans_currency_input == "GBP":
         trans_currency = Currency.GBP
     else:
         trans_currency = Currency.AED

     # Transaction date & time
     trans_date_time_input = input("Transaction date - 'now' or YYYY-MM-DD hh:mm:ss: ")
     if trans_date_time_input == "now":
         trans_date_time = datetime.datetime.now()
     else:
         trans_date_time = datetime.datetime.strptime(
                             trans_date_time_input,
                             "%Y-%m-%d %H:%M:%S")

     # Create an object of class Transaction
     transaction = Transaction(transaction_type=trans_type,
                               amount=trans_amount,
                               currency=trans_currency,
                               description=trans_description,
                               date_time=trans_date_time)

     # Add the newly created transaction to the list of transactions
     self.__transactions.append(transaction)
     return transaction

 def get_total_amount(self):
     total = 0
     # For each transaction,  read the amount and then add it to the total
     for transaction in self.__transactions:
         total += transaction.get_trans_amount()
     return total

 # Print the transactions
 def print_transactions(self):
     for transaction in self.__transactions:
         print(transaction)

 #Convert transacitons into a dictionary for json serialization
 def to_dict(self):
     transactions_list=[]
     manager_dict={}
     for transaction in self.__transactions:
        # Convert each transaction into a string format
        transactions_list.append(transaction.to_dict())
     manager_dict["transactions"] =transactions_list
     return manager_dict

 # Decode JSON data and convert to transaction list
 def decode(self, jsonItem):
     if "__trans_id" in jsonItem and "__trans_type" in jsonItem and "__trans_amount" in jsonItem \
             and "__trans_description" in jsonItem and "__trans_currency" in jsonItem and "__trans_date_time" in jsonItem:

         transaction = Transaction(TransactionType[jsonItem["__trans_type"]],
                           jsonItem["__trans_amount"],
                           Currency[jsonItem["__trans_currency"]],
                           jsonItem["__trans_description"],
                           datetime.datetime.strptime(jsonItem["__trans_date_time"], "%Y-%m-%d %H:%M:%S"))
         return self.__transactions.append(transaction)
     return jsonItem

# Create a Transaction Manager object
trans_manager = TransactionManager()

# Create two transactions defined by the user
for counter in range(2):
 trans_manager.create_transaction()
 trans_manager.print_transactions()
 print("Balance Amount: {amount}".format(
     amount=trans_manager.get_total_amount()))

# Serialize data using Pickle for Transaction object
file_handler = open('transaction_data.pkl', 'wb')
pickle.dump(trans_manager, file_handler)
file_handler.close()

# Unpickle data using pickle to get back the Transaction object
file_handler = open('transaction_data.pkl', 'rb')
loaded_trans_manager = pickle.load(file_handler)
file_handler.close()

# Print deserialized data
print("\nDeserialized Data from Pickle:")
loaded_trans_manager.print_transactions()
print("Balance Amount: {amount}".format(amount=loaded_trans_manager.get_total_amount()))

# Serialize data using JSON
file_handler= open('transactions.json', 'w')
json.dump(loaded_trans_manager.to_dict(), file_handler)
file_handler.close()

# Create a new TransactionManager object to load data from json
new_trans_manager = TransactionManager()
# Deserialize JSON data from the file
file_handler_json = open("transactions.json", "rb")
# Decode JSON data using json.load with the custom decoder
json.load(file_handler_json, object_hook=new_trans_manager.decode)
file_handler_json.close()

# Print deserialized data from JSON
print("\nDeserialized Data from JSON:")
new_trans_manager.print_transactions()
print("Balance Amount:{amount}".format(amount=new_trans_manager.get_total_amount()))
