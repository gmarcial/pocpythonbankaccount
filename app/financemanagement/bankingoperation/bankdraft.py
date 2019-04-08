from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountTypeRulesFactory

class BankDraft():
    
    def __init__(self, target, transferamount):

        if(type(target) != BankAccount):
            raise TypeError(f"The type informed is invalid for the context {target}")
        if(type(transferamount) != Amount):
            raise TypeError(f"The type informed is invalid for the context {transferamount}")
        
        self.__target = target
        self.__transferamount = transferamount
    
    def towithdraw(self):

        accounttyperulesfactory = AccountTypeRulesFactory()

        targetaccounttyperules = accounttyperulesfactory.make(self.__target.gettype())
        targetaccounttyperules.checklimitwithdrawal(self.__transferamount)
        self.__target.withdraw(self.__transferamount)