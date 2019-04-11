from app.financemanagement.amount import Amount
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.infrasctructure import Session
from app.financemanagement.bankingoperation.banktransfer import BankTransfer
from app.financemanagement.infrasctructure.repository import BankAccountRepository, BankTransactionRecordRepository

class ToTransfer():

    def __init__(self):
        #unitofwork is better? 
        self.__session = Session()
        self.__bankaccountrepository = BankAccountRepository(self.__session)
        self.__banktransactionrecordrepository = BankTransactionRecordRepository(self.__session)

    def execute(self, senderaccountnumber, receiveraccountnumber, transferamount):
        
        #Validar targetaccountnumber
        transferamount = Amount(transferamount)
        
        senderaccount = self.__bankaccountrepository.findperaccountnumber(senderaccountnumber)
        receiveraccount = self.__bankaccountrepository.findperaccountnumber(receiveraccountnumber)

        banktransfer = BankTransfer(senderaccount, receiveraccount, transferamount)
        banktransactionrecords = banktransfer.transfer()
        
        self.__bankaccountrepository.update(senderaccount)
        self.__bankaccountrepository.update(receiveraccount)
        self.__banktransactionrecordrepository.addmultiple(banktransactionrecords)
        self.__session.commit()