from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.bankingoperation.banktransactionrecord import BankOperationType
from app.financemanagement.bankingoperation.banktransactionrecord import BankTransactionRecord
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountType
from app.financemanagement.infrasctructure.mapping import BankAccountMap
from app.financemanagement.infrasctructure.mapping import BankAccountMap, BankTransactionRecordMap


class BankAccountRepository():

    def __init__(self, session):
        self.__session = session

    def add(self, newbankaccount):

        # Convert obj core to => infra
        #TODO: Encapsulat
        number = newbankaccount.getnumber()
        balance = newbankaccount.getbalance()
        type = newbankaccount.gettype()
        bankaccountmap = BankAccountMap(
            number=number, balance=balance.getvalue(), type=type.value)

        self.__session.add(bankaccountmap)

    def findperaccountnumber(self, targetaccountnumber):

        bankcccountmap = self.__session.query(BankAccountMap).filter_by(
            number=targetaccountnumber).first()

        #TODO: Possible encapsulation
        number = bankcccountmap.number
        balance = Amount(bankcccountmap.balance)
        accounttype = AccountType(bankcccountmap.type)
        id = bankcccountmap.id

        return BankAccount(number, balance, accounttype, id)

    def update(self, bankaccount):
        
        number = bankaccount.getnumber()
        balance = bankaccount.getbalance().getvalue()

        self.__session.query(BankAccountMap).filter_by(number=number).update({"balance": balance})

    def all(self):
        return self.__session.query(BankAccountMap).all()


class BankTransactionRecordRepository():

    def __init__(self, session):
        self.__session = session

    def add(self, newbanktransactionrecord):

        #TODO: Encapsulat
        operation = newbanktransactionrecord.getoperation().value
        whenoccurred = newbanktransactionrecord.getwhenoccurred()
        amount = newbanktransactionrecord.getamount()
        description = newbanktransactionrecord.getdescription()
        contaid = newbanktransactionrecord.getcontaid()
        
        banktransactionrecordmap = BankTransactionRecordMap(
            operation=operation, whenoccurred=whenoccurred, amount=amount, description=description, contaid=contaid)

        self.__session.add(banktransactionrecordmap)
    
    def addmultiple(self, newbanktransactionrecords):

        for newbanktransactionrecord in newbanktransactionrecords:

            #TODO: Encapsulat
            operation = newbanktransactionrecord.getoperation().value
            whenoccurred = newbanktransactionrecord.getwhenoccurred()
            amount = newbanktransactionrecord.getamount()
            description = newbanktransactionrecord.getdescription()
            contaid = newbanktransactionrecord.getcontaid()
        
            banktransactionrecordmap = BankTransactionRecordMap(
                operation=operation, whenoccurred=whenoccurred, amount=amount, description=description, contaid=contaid)

            self.__session.add(banktransactionrecordmap)

    def all(self, number):
        return self.__session.query(BankTransactionRecordMap).filter_by(number=number).all()
