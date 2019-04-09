from datetime import datetime
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountTypeRulesFactory
from app.financemanagement.bankingoperation.banktransactionrecord import BankTransactionRecord
from app.financemanagement.bankingoperation.bankoperationtype import BankOperationType


class BankDraft():
    
    def __init__(self, target, withdrawamount):

        if(type(target) != BankAccount):
            raise TypeError(f"The type informed is invalid for the context {target}")
        if(type(withdrawamount) != Amount):
            raise TypeError(f"The type informed is invalid for the context {withdrawamount}")
        
        self.__target = target
        self.__withdrawamount = withdrawamount
        self.__bankoperationtype = BankOperationType.WITHDRAW
    
    def towithdraw(self):

        accounttyperulesfactory = AccountTypeRulesFactory()

        targetaccounttyperules = accounttyperulesfactory.make(self.__target.gettype())
        targetaccounttyperules.checklimitwithdrawal(self.__withdrawamount)
        self.__target.withdraw(self.__withdrawamount)

        recorddescription = "Saque em conta bancaria"
        recorddepositamount = -int(self.__withdrawamount)
        return BankTransactionRecord(self.__bankoperationtype, datetime.now(), recorddepositamount, recorddescription, self.__target.getid())