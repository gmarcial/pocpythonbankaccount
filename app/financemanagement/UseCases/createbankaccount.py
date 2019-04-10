import random
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountType
from app.financemanagement.infrasctructure import Session
from app.financemanagement.infrasctructure.repository import BankAccountRepository

class CreateBankAccount():

    def __init__(self):
        #unitofwork is better? 
        self.__session = Session()
        self.__bankaccountrepository = BankAccountRepository(self.__session)

    def execute(self, balance, accounttype):
        
        number = str(random.randint(1,999999999999999999))
        balance = Amount(balance)
        accounttype = AccountType(accounttype)
        newbankaccount = BankAccount(number, balance, accounttype)
        
        self.__bankaccountrepository.add(newbankaccount)
        self.__session.commit()