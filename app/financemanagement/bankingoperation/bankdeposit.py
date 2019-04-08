from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountTypeRulesFactory

class BankDeposit():

    def __init__(self, receiver, transferamount):
        
        if(type(receiver) != BankAccount):
            raise TypeError(f"The type informed is invalid for the context {receiver}")
        if(type(transferamount) != Amount):
            raise TypeError(f"The type informed is invalid for the context {transferamount}")
        
        self.__receiver = receiver
        self.__transferamount = transferamount

    def todeposit(self):

        accounttyperulesfactory = AccountTypeRulesFactory()

        receiveraccounttyperules = accounttyperulesfactory.make(self.__receiver.gettype())
        receiveraccounttyperules.checklimitreceive(self.__transferamount)
        self.__receiver.receive(self.__transferamount)