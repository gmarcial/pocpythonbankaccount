from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.infrasctructure import Session
from app.financemanagement.bankingoperation.bankdeposit import BankDeposit
from app.financemanagement.infrasctructure.repository import BankAccountRepository, BankTransactionRecordRepository

class ToDeposit():

    def __init__(self):
        #unitofwork is better? 
        self.__session = Session()
        self.__bankaccountrepository = BankAccountRepository(self.__session)
        self.__banktransactionrecordrepository = BankTransactionRecordRepository(self.__session)

    def execute(self, receiveraccountnumber, depositamount):
        
        #Validar targetaccountnumber

        receiveraccount = self.__bankaccountrepository.findperaccountnumber(receiveraccountnumber)
        bankdeposit = BankDeposit(receiveraccount, depositamount)
        banktransactionrecord = bankdeposit.todeposit()
        
        self.__bankaccountrepository.update(receiveraccount)
        self.__banktransactionrecordrepository.add(banktransactionrecord)
        self.__session.commit()