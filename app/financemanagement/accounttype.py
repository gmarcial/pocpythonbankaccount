from enum import Enum
from app.financemanagement.amount import Amount

class AccountType(Enum):
    SAVINGS = 0
    CHECKING = 1

    def __int__(self):
        self.value

class SavingsAccountTypeRules:

    def __init__(self):
        self.__SAVINGS_LIMIT_WITHDRAWAL = Amount(2500)
        self.__SAVINGS_LIMIT_RECEIVE = Amount(5000)
    
    def checklimitwithdrawal(self, amount):
        if amount > self.__SAVINGS_LIMIT_WITHDRAWAL:
            raise ValueError("The amount exceeds the limit of withdrawal for a savings account")
    
    def checklimitreceive(self, amount):
        if amount > self.__SAVINGS_LIMIT_RECEIVE:
            raise ValueError("The amount exceeds the limit of receive for a savings account")

class CheckingAccountTypeRules:
    
    def __init__(self):
        self.__CHECKING_LIMIT_WITHDRAWAL = Amount(6000)
        self.__CHECKING_LIMIT_RECEIVE = Amount(8000)
    
    def checklimitwithdrawal(self, amount):
        if amount > self.__CHECKING_LIMIT_WITHDRAWAL:
            raise ValueError("The amount exceeds the limit of withdrawal for a checking account")
    
    def checklimitreceive(self, amount):
        if amount > self.__CHECKING_LIMIT_RECEIVE:
            raise ValueError("The amount exceeds the limit of receive for a checking account")

class AccountTypeRulesFactory:

    def make(self, accounttype):

        if(type(accounttype) != AccountType):
            raise TypeError(f"The type informed is invalid for the context {accounttype}")

        if accounttype == AccountType.SAVINGS:
            return SavingsAccountTypeRules()
        if accounttype == AccountType.CHECKING:
            return CheckingAccountTypeRules()
        else:
            raise ValueError(f"The account type informed is invalid {accounttype}")