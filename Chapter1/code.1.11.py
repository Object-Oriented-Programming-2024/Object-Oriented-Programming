import datetime
from enum import Enum


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
    transaction_count = 0  # a static variable that keeps track of the number of transactions

    # Initialize the Transaction class
    def __init__(self, transaction_type, amount, currency, description, date_time):
        # Increment the number of transactions with the creation of a new transaction
        Transaction.transaction_count += 1

        # Assign a unique transaction ID based on the number of transactions
        self.__trans_id = "T" + str(Transaction.transaction_count)
        self.__trans_type = transaction_type
        self.trans_amount = amount
        self.__trans_description = description
        self.__trans_currency = currency
        self.__trans_date_time = date_time

    def get_trans_id(self):
        return self.__trans_id

    def get_transaction_type(self):
        return self.__trans_type

    def get_trans_amount(self):
        return self.trans_amount

    def get_trans_date_time(self):
        return self.__trans_date_time

    def get_trans_currency(self):
        return self.__trans_currency

    def get_trans_description(self):
        return self.__trans_description

    def set_trans_description(self, description):
        self.__trans_description = description

    # Define a string representation of the transaction
    def __str__(self):
        return ("Transaction ID: {id}, Amount: {amount} {currency}, Type: ({type}), "
                "Description: {description}, Date & Time: {date_time}"
                .format(id=self.__trans_id, amount=self.trans_amount,
                        currency=Currency(self.__trans_currency).name,
                        type=TransactionType(self.__trans_type).name,
                        description=self.__trans_description,
                        date_time=self.__trans_date_time))


class TransactionManager:
    """This class keeps track of transactions and allows users
    to create transactions, and calculate their total amount
    """

    def __init__(self):

        # Define the transactions managed by TransactionManager as an empty list
        self.__transactions = []

    # A function that allows the creation of a transaction
    def create_transaction(self):
        trans_type_input = input("What type of transaction is it (Expense/Income)?")
        trans_type = TransactionType.EXPENSE
        if trans_type_input == "Income":
            trans_type = TransactionType.INCOME
        trans_amount = float(input("What's the amount of the transaction? Please enter a number"))

        if trans_type == TransactionType.EXPENSE:
            trans_amount *= -1
        trans_description = input("What's the transaction description?")
        trans_currency_input = input("What's the transaction Currency (USD/EUR/GBP/AED)?")

        trans_currency = Currency.USD
        if trans_currency_input == "EUR":
            trans_currency = Currency.EUR
        elif trans_currency_input == "GBP":
            trans_currency = Currency.GBP
        elif trans_currency_input == "AED":
            trans_currency = Currency.AED
        trans_date_time_input = input(
            "When did the transaction happen (You can type 'now' or a date/time in this format: YYYY MM DD hh mm ss)")

        trans_date_time = datetime.datetime.now()
        datetime_tokens = trans_date_time_input.split(" ")

        # If the user provides 6 numbers according to the provided format,
        # They will be used to build a date time attribute
        if len(datetime_tokens) == 6:
            trans_date_time = datetime.datetime(int(datetime_tokens[0]),
                                                int(datetime_tokens[1]),
                                                int(datetime_tokens[2]),
                                                int(datetime_tokens[3]),
                                                int(datetime_tokens[4]),
                                                int(datetime_tokens[5]))

        # Create an object of class Transaction
        transaction = Transaction(transaction_type=trans_type, amount=trans_amount,
                                  currency=trans_currency, description=trans_description,
                                  date_time=trans_date_time)

        # Add the newly created transaction to the list of transactions
        self.__transactions.append(transaction)
        return transaction

    def get_total_amount(self):
        total = 0

        # For each transaction, we read the amount and then add it to the total
        for transaction in self.__transactions:
            total += transaction.get_trans_amount()
        return total

    def print_transactions(self):  # print the transactions
        for transaction in self.__transactions:
            print(transaction)


trans_manager = TransactionManager()  # create a TransactionManager object

# Create three transactions defined by the user
t1 = trans_manager.create_transaction()
t2 = trans_manager.create_transaction()
t3 = trans_manager.create_transaction()
trans_manager.print_transactions()  # print all the created transactions

# show the total amount of transactions
print("Total Amount:{amount}".format(amount=trans_manager.get_total_amount()))