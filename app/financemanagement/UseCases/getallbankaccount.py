import random
from app.financemanagement.infrasctructure import Session
from app.financemanagement.infrasctructure.repository import BankAccountRepository

class GetAllBankAccount():

    def __init__(self):
        #unitofwork is better? 
        self.__session = Session()
        self.__bankaccountrepository = BankAccountRepository(self.__session)

    def execute(self):
        return self.__bankaccountrepository.all()