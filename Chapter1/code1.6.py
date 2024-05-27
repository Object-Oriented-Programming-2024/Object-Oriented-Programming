class BankAccount:
 interest_rate=0.05
 def __init__(self,balance,account_number,person_name,person_address):
     self.balance=balance
     self.account_number=account_number
     self.person_name=person_name
     self.person_address=person_address

 # Define a method to deposit money into the account.
 def deposit(self,amount):
     if amount>=0:
         self.balance+=amount

 # Define a method to withdraw money from the account.
 def withdraw(self,amount):
     if amount<=self.balance:
         self.balance-=amount

 # The methods below represent the Setter and Getter methods
 def get_balance(self):
     return self.balance

 def get_account_number(self):
     return self.account_number

 def get_person_name(self):
     return self.person_name

 def get_person_address(self):
     return self.person_address

 def set_person_address(self,person_address):
     self.person_address=person_address

 def calculate_interest(amount):
     return BankAccount.interest_rate * amount

# Create two instances of BankAccount
bank_account_1=BankAccount(balance=1000,account_number="1234",
                        person_name="Ahmed Ali",person_address="Main Street")
bank_account_2=BankAccount(balance=500,account_number="1235",
                         person_name="John Smith",person_address="Vivion Rd")

# The below line  will access the account number of object bank_account_1
print("Bank No: ",bank_account_1.get_account_number())
print("Depositing 50 from the account")

# The below line will access the deposit method of object bank_account_1
bank_account_1.deposit(50)

# The below line will access the balance of object bank_account_1
print("Balance: ",bank_account_1.get_balance())

# The below line  will set the address of object bank_account_1
bank_account_1.set_person_address("Union Str")

# The below line  will access the person name of object bank_account_1
print("Bank Person Name: ",bank_account_1.get_person_name())

# The below will retrieve the static variable interest_rate
print("Interest Rate: ",BankAccount.interest_rate)

# The below will call the static method calculate_interest
print("Interest: ",BankAccount.calculate_interest(bank_account_1.get_balance()))
