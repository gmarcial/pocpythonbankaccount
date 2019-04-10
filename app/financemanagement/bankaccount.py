import random
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountType

class BankAccount(object):
    
    def __init__(self, number, balance, accounttype, id = 0):
        
        if(type(balance) != Amount):
            raise TypeError(f"The type informed is invalid for the context {balance}")
        if(type(accounttype) != AccountType):
            raise TypeError(f"The type informed is invalid for the context {accounttype}")
        #Create a test for this
        if(type(number) != str or len(number) < 0):
            raise TypeError(f"The type informed is invalid for the context {number}")

        self.__id = id
        self.__number = number
        self.__balance = balance
        self.__type = accounttype

    def receive(self, amount):
        
        if(type(amount) != Amount):
            raise TypeError(f"The type informed is invalid for the context {amount}")
        
        self.__balance += amount
    
    def withdraw(self, amount):

        if(type(amount) != Amount):
            raise TypeError(f"The type informed is invalid for the context {amount}")

        if(self.__balance < amount):
            raise ValueError("Insufficient balance for a withdraw operation")

        self.__balance -= amount

    def getbalance(self):
        return self.__balance
    
    def gettype(self):
        return self.__type
    
    def getid(self):
        return self.__id
    
    def getnumber(self):
        return self.__number