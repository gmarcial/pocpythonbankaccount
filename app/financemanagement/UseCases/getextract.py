import random
from app.financemanagement.infrasctructure import Session
from app.financemanagement.infrasctructure.repository import BankTransactionRecordRepository

class GetExtract():

    def __init__(self):
        #unitofwork is better? 
        self.__session = Session()
        self.__banktransactionrecordrepository = BankTransactionRecordRepository(self.__session)

    def execute(self, targetaccountnumber):
        return self.__banktransactionrecordrepository.all(targetaccountnumber)