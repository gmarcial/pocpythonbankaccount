from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.bankingoperation.banktransactionrecord import BankOperationType
from app.financemanagement.bankingoperation.banktransactionrecord import BankTransactionRecord
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountType
from app.financemanagement.infrasctructure.mapping import BankAccountMap
from app.financemanagement.infrasctructure.mapping import BankAccountMap, BankAccountModel, BankTransactionRecordMap, BankTransactionRecordModel


class BankAccountRepository():

    def __init__(self, session):
        self.__session = session

    def add(self, newbankaccount):

        # Convert obj core to => infra
        # TODO: Encapsulat
        number = newbankaccount.getnumber()
        balance = newbankaccount.getbalance()
        type = newbankaccount.gettype()
        bankaccountmap = BankAccountMap(
            number=number, balance=balance.getvalue(), type=type.value)

        self.__session.add(bankaccountmap)

    def findperaccountnumber(self, targetaccountnumber):

        bankcccountmap = self.__session.query(BankAccountMap).filter_by(
            number=targetaccountnumber).first()

        # TODO: Possible encapsulation
        number = targetaccountnumber
        balance = Amount(bankcccountmap.balance)
        accounttype = AccountType(bankcccountmap.type)
        id = bankcccountmap.id

        return BankAccount(number, balance, accounttype, id)

    def findperaccountnumberreturnmodel(self, targetaccountnumber):

        bankcccountmap = self.__session.query(BankAccountMap).filter_by(
            number=targetaccountnumber).first()

        id = bankcccountmap.id
        number = bankcccountmap.number
        # Decimal(orm) => integer(python)
        balance = int(bankcccountmap.balance)
        type = bankcccountmap.type

        return BankAccountModel(id, number, balance, type)

    def update(self, bankaccount):

        number = bankaccount.getnumber()
        balance = bankaccount.getbalance().getvalue()

        self.__session.query(BankAccountMap).filter_by(
            number=number).update({"balance": balance})

    def all(self):
        bankaccountsmaplist = self.__session.query(BankAccountMap).all()

        bankaccountmodellist = []
        for bankaccountmap in bankaccountsmaplist:

            id = bankaccountmap.id
            number = bankaccountmap.number
            # Decimal(orm) => integer(python)
            balance = int(bankaccountmap.balance)
            type = bankaccountmap.type

            bankaccountmodellist.append(
                BankAccountModel(id, number, balance, type))

        return bankaccountmodellist


class BankTransactionRecordRepository():

    def __init__(self, session):
        self.__session = session

    def add(self, newbanktransactionrecord):

        # TODO: Encapsulat
        operation = newbanktransactionrecord.getoperation().value
        whenoccurred = newbanktransactionrecord.getwhenoccurred()
        amount = newbanktransactionrecord.getamount()
        description = newbanktransactionrecord.getdescription()
        contaid = newbanktransactionrecord.getcontaid()
        number = newbanktransactionrecord.getnumber()

        banktransactionrecordmap = BankTransactionRecordMap(
            operation=operation, number=number, whenoccurred=whenoccurred, amount=amount, description=description, contaid=contaid)

        self.__session.add(banktransactionrecordmap)

    def addmultiple(self, newbanktransactionrecords):

        for newbanktransactionrecord in newbanktransactionrecords:

            # TODO: Encapsulat
            operation = newbanktransactionrecord.getoperation().value
            whenoccurred = newbanktransactionrecord.getwhenoccurred()
            amount = newbanktransactionrecord.getamount()
            description = newbanktransactionrecord.getdescription()
            contaid = newbanktransactionrecord.getcontaid()
            number = newbanktransactionrecord.getnumber()

            banktransactionrecordmap = BankTransactionRecordMap(
                operation=operation, number=number, whenoccurred=whenoccurred, amount=amount, description=description, contaid=contaid)

            self.__session.add(banktransactionrecordmap)

    def all(self, number):
        banktransactionrecordmaplist = self.__session.query(
            BankTransactionRecordMap).filter_by(number=number).all()

        banktransactionmodellist = []

        for banktransactionrecordmap in banktransactionrecordmaplist:

            id = banktransactionrecordmap.id
            operation = banktransactionrecordmap.operation
            number = banktransactionrecordmap.number
            whenoccurred = str(banktransactionrecordmap.whenoccurred)
            amount = int(banktransactionrecordmap.amount)
            description = banktransactionrecordmap.description
            contaid = banktransactionrecordmap.contaid

            banktransactionmodellist.append(
                BankTransactionRecordModel(
                    id, operation, number, whenoccurred, amount, description, contaid))
        
        return banktransactionmodellist
