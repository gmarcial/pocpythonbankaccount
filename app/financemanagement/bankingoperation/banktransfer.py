from datetime import datetime
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountTypeRulesFactory
from app.financemanagement.bankingoperation.banktransactionrecord import BankTransactionRecord
from app.financemanagement.bankingoperation.bankoperationtype import BankOperationType


class BankTransfer(object):

    def __init__(self, sender, receiver, transferamount):

        if(type(sender) != BankAccount):
            raise TypeError(
                f"The type informed is invalid for the context {sender}")
        if(type(receiver) != BankAccount):
            raise TypeError(
                f"The type informed is invalid for the context {receiver}")
        if(type(transferamount) != Amount):
            raise TypeError(
                f"The type informed is invalid for the context {transferamount}")

        self.__sender = sender
        self.__receiver = receiver
        self.__transferamount = transferamount
        self.__bankoperationtype = BankOperationType.TRANSFER

    def transfer(self):

        accounttyperulesfactory = AccountTypeRulesFactory()

        senderaccounttyperules = accounttyperulesfactory.make(
            self.__sender.gettype())
        senderaccounttyperules.checklimitwithdrawal(self.__transferamount)
        self.__sender.withdraw(self.__transferamount)

        recorddescription = f"Transferencia ocorrida no valor {self.__transferamount.getvalue()} com o remetente do numero de conta {self.__sender.getnumber()} e destinatario com numero de conta {self.__receiver.getnumber()}"
        whenoccurred = datetime.now()

        receiveraccounttyperules = accounttyperulesfactory.make(
            self.__receiver.gettype())
        receiveraccounttyperules.checklimitreceive(self.__transferamount)
        self.__receiver.receive(self.__transferamount)

        sendernumber = self.__sender.getnumber()
        recordsenderamount = -int(self.__transferamount)
        banktransactionrecordsender = BankTransactionRecord(
            self.__bankoperationtype, sendernumber, whenoccurred, recordsenderamount, recorddescription, self.__sender.getid())
        
        receivernumber = self.__receiver.getnumber()
        recordreceiveramount = +int(self.__transferamount)
        banktransactionrecordreceiver = BankTransactionRecord(
            self.__bankoperationtype, receivernumber, whenoccurred, recordreceiveramount, recorddescription, self.__receiver.getid())

        return (banktransactionrecordsender, banktransactionrecordreceiver)
