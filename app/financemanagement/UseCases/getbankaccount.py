import random
from app.financemanagement.infrasctructure import Session
from app.financemanagement.infrasctructure.repository import BankAccountRepository

class GetBankAccount():

    def __init__(self):
        #unitofwork is better? 
        self.__session = Session()
        self.__bankaccountrepository = BankAccountRepository(self.__session)

    def execute(self, accountnumber):
        return self.__bankaccountrepository.findperaccountnumber(accountnumber)