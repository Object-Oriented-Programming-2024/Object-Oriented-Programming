from bank_account import BankAccount
import pickle
import os

class BankSystem:
    def __init__(self,name, filename):
        self.__bank_name=name
        self.__filename=filename
        self.__accounts=self.read_accounts_from_file()

    def setName(self, name):
        self.__bank_name=name

    def getName(self):
        return self.__bank_name

    def getAccounts(self):
        return self.__accounts

    def addAccount(self,firstName,lastName,accountNumber,balance):
            if not accountNumber in self.__accounts:
                account=BankAccount(firstName=firstName,lastName=lastName,accountNumber=accountNumber,balance=balance)
                self.__accounts[accountNumber]=account
            else:
                raise Exception(f"Sorry. This Account Number ='{accountNumber}' already exists.")

    def findAccount(self,accountNumber):
            if accountNumber in self.__accounts:
                return self.__accounts[accountNumber]
            raise Exception(f"Account Number ='{accountNumber}' not found")

    def deleteAccount(self,accountNumber):
            if accountNumber in self.__accounts:
                del self.__accounts[accountNumber]
                return "Deleted Successfully"
            raise Exception(f"Account Number ='{accountNumber}' not found")

    def transfer(self,fromAccountNumber,toAccountNumber,amount):
        try:
            fromAccount=self.findAccount(fromAccountNumber)
            toAccount=self.findAccount(toAccountNumber)
            fromAccount.withdraw(amount)
            toAccount.deposit(amount)

        except Exception as e:
            raise e

    def read_accounts_from_file(self):
        try:
            # Check if the file exists
            if not os.path.exists(self.__filename):
                # If the file doesn't exist, create it and write an empty dictionary
                with open(self.__filename, 'wb') as file:
                    self.__accounts={}
                    file.close()

            else:
                # Now open the file in read mode ('rb')
                with open(self.__filename, 'rb') as file:
                    # Load the data from the file
                    self.__accounts = pickle.load(file)
                    file.close()
            return self.__accounts
        except:
            raise Exception("Unable to read from the Bank Accounts File")

    def write_customers_to_file(self):
            try:
                with open(self.__filename, 'wb') as f:
                    pickle.dump(self.__accounts,f)
                    f.close()
            except:
                raise Exception("Unable to write to the Bank Accounts File")

try:
 main_bank=BankSystem("First UAE Bank","bank_accounts_details.pkl")
 main_bank.addAccount("Rauda","Said","7",10000)
 main_bank.addAccount("Ahmed","Ali","2",500)
 main_bank.transfer("1","2",400)
 main_bank.write_customers_to_file()
 print("The End")

except Exception as e:
 print(e)
