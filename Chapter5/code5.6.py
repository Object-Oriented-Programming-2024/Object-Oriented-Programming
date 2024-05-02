class BankAccount: # Class to represent a Bank Account
 def __init__(self, first_name, last_name, account_number, balance=0):
     self._first_name = first_name
     self._last_name = last_name
     self._account_number = account_number
     self._balance = balance

 def get_balance(self):
     return self._balance

 def deposit(self, amount):
     if amount > 0:
         self._balance += amount
         print(f"Deposited: {amount}. New Balance: {self._balance}")

 def withdraw(self, amount):
 # This method withdraws specified amount if sufficient balance is available.
     if 0 < amount <= self._balance:
         self._balance -= amount
         print(f"Withdrawn: {amount}. New Balance: {self._balance}")
     else:
         print("Insufficient balance for the withdrawal.")


# Class to represent a savings account, inheriting from BankAccount.
class SavingsAccount(BankAccount):
 def __init__(self, first_name, last_name, account_number, interest_rate, balance=0):
     super().__init__(first_name, last_name, account_number, balance)
     self._interest_rate = interest_rate

 # This method overrides the deposit method to include interest calculation
 def deposit(self, amount):
     if amount > 0:
         interest = amount * self._interest_rate
         self._balance += amount + interest
         print(f"Deposited: {amount}. Interest: {interest}. New Balance: {self._balance}")


# Example Usage
account = BankAccount("John", "Doe", "123456789", 1000)
account.deposit(200)
account.withdraw(500)

savings_account = SavingsAccount("Jane", "Doe", "987654321", 0.05, 1000)
savings_account.deposit(200)
savings_account.withdraw(500)
