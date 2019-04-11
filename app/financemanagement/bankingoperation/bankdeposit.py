from datetime import datetime
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountTypeRulesFactory
from app.financemanagement.bankingoperation.banktransactionrecord import BankTransactionRecord
from app.financemanagement.bankingoperation.bankoperationtype import BankOperationType


class BankDeposit():

    def __init__(self, receiver, depositamount):

        if(type(receiver) != BankAccount):
            raise TypeError(
                f"The type informed is invalid for the context {receiver}")
        if(type(depositamount) != Amount):
            raise TypeError(
                f"The type informed is invalid for the context {depositamount}")

        self.__receiver = receiver
        self.__depositamount = depositamount
        self.__bankoperationtype = BankOperationType.DEPOSIT

    def todeposit(self):

        accounttyperulesfactory = AccountTypeRulesFactory()

        receiveraccounttyperules = accounttyperulesfactory.make(
            self.__receiver.gettype())
        receiveraccounttyperules.checklimitreceive(self.__depositamount)
        self.__receiver.receive(self.__depositamount)

        number = self.__receiver.getnumber()
        recorddescription = "Depositado em conta bancaria"
        recorddepositamount = +int(self.__depositamount)
        return BankTransactionRecord(
            self.__bankoperationtype, number, datetime.now(), recorddepositamount, recorddescription, self.__receiver.getid())
