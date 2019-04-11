from app.financemanagement.bankingoperation.bankoperationtype import BankOperationType
from datetime import datetime
from app.financemanagement.amount import Amount

class BankTransactionRecord():
    
    def __init__(self, operation, number, whenoccurred, amount, description, contaid):
        
        #Add property number...

        if(type(operation) != BankOperationType):
            raise TypeError(f"The type informed is invalid for the context {operation}")
        if(type(whenoccurred) != datetime):
            raise TypeError(f"The type informed is invalid for the context {whenoccurred}")
        if(type(amount) != int):
            raise TypeError(f"The type informed is invalid for the context {amount}")
        if(type(description) != str):
            raise TypeError(f"The type informed is invalid for the context {description}")
        if(description != None and len(description) < 10):
            raise ValueError(f"The description informed should be equal or greater than 30 characters {description}")
        if(contaid <= 0):
            raise TypeError(f"The type informed is invalid for the context {contaid}")
        #Create a test for this
        if(type(number) != str or len(number) < 0):
            raise TypeError(f"The type informed is invalid for the context {number}")

        self.__operation = operation
        self.__number = number
        self.__whenoccurred = whenoccurred
        self.__amount = amount
        self.__description = description
        self.__contaid = contaid

    def getoperation(self):
        return self.__operation

    def getnumber(self):
        return self.__number

    def getwhenoccurred(self):
        return self.__whenoccurred

    def getamount(self):
        return self.__amount

    def getdescription(self):
        return self.__description
    
    def getcontaid(self):
        return self.__contaid