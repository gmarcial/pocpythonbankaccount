from app.financemanagement.amount import Amount
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.infrasctructure import Session
from app.financemanagement.bankingoperation.bankdraft import BankDraft
from app.financemanagement.infrasctructure.repository import BankAccountRepository, BankTransactionRecordRepository

class ToWithdraw():

    def __init__(self):
        #unitofwork is better? 
        self.__session = Session()
        self.__bankaccountrepository = BankAccountRepository(self.__session)
        self.__banktransactionrecordrepository = BankTransactionRecordRepository(self.__session)

    def execute(self, targetaccountnumber, withdrawamount):
        
        #Validar targetaccountnumber
        withdrawamount = Amount(withdrawamount)

        targetaccount = self.__bankaccountrepository.findperaccountnumber(targetaccountnumber)
        bankdraft = BankDraft(targetaccount, withdrawamount)
        banktransactionrecord = bankdraft.towithdraw()
        
        self.__bankaccountrepository.update(targetaccount)
        self.__banktransactionrecordrepository.add(banktransactionrecord)
        self.__session.commit()