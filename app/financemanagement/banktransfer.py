from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountTypeRulesFactory

class BankTransfer(object):

    def __init__(self, sender, receiver, transferamount):
        
        if(type(sender) != BankAccount):
            raise TypeError(f"The type informed is invalid for the context {sender}")
        if(type(receiver) != BankAccount):
            raise TypeError(f"The type informed is invalid for the context {receiver}")
        if(type(transferamount) != Amount):
            raise TypeError(f"The type informed is invalid for the context {transferamount}")

        self.__sender = sender
        self.__receiver = receiver
        self.__transferamount = transferamount

    def transfer(self):
        
        accounttyperulesfactory = AccountTypeRulesFactory()

        senderaccounttyperules = accounttyperulesfactory.make(self.__sender.gettype())
        senderaccounttyperules.checklimitwithdrawal(self.__transferamount)
        self.__sender.withdraw(self.__transferamount)

        receiveraccounttyperules = accounttyperulesfactory.make(self.__receiver.gettype())
        receiveraccounttyperules.checklimitreceive(self.__transferamount)
        self.__receiver.receive(self.__transferamount)