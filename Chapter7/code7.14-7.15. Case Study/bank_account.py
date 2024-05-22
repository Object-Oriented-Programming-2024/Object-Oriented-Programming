class BankAccount:
    """this class represents a bank account"""
    def __init__(self,firstName="",lastName="",accountNumber="",balance=0.0):
        self.__firstName=firstName
        self.__lastName=lastName
        self.__accountNumber=accountNumber
        assert balance>=0 # we want to make sure the balance is at least 0 AED
        self.__balance=balance

    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getAccountNumber(self):
        return self.__accountNumber
    def getBalance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount>self.__balance:
            raise Exception("The amount is greater than the balance")
        self.__balance-=amount
    def deposit(self,amount):
        if amount<=0:
            raise Exception("Amount should be greater than zero")
        self.__balance+=amount
