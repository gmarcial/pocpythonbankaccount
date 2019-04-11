import unittest
from uuid import uuid4
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.accounttype import AccountType
from app.financemanagement.amount import Amount

class TestBankAccount(unittest.TestCase):
    
    def test_should_be_created_bank_account_in_valid_state(self):
        
        balance = Amount(0)
        account = BankAccount("123", balance, AccountType.SAVINGS)

        self.assertIsInstance(account, BankAccount)
        self.assertIsNotNone(account)

    
    def test_should_not_be_created_bank_account_with_invalid_balance(self):
        
        balance = "123"
        
        with self.assertRaises(TypeError):
            BankAccount("123", balance, AccountType.SAVINGS)
    
    def test_should_not_be_created_bank_account_with_invalid_account_type(self):
        
        balance = Amount(0)

        with self.assertRaises(TypeError):
            BankAccount("123", balance, 22)
    
    def test_should_receive_an_amount_and_increase_the_current_amount(self):

        initialbalance = Amount(0)

        account = BankAccount("123", initialbalance, AccountType.SAVINGS)

        receiveAmount = Amount(100)
        account.receive(receiveAmount)
        newbalance = account.getbalance()

        expectedbalance = (initialbalance + receiveAmount)

        self.assertEqual(newbalance, expectedbalance)

    def test_should_not_receive_an_amount_when_amount_is_invalid(self):

        initialbalance = Amount(0)

        account = BankAccount("123", initialbalance, AccountType.SAVINGS)

        receiveAmount = 100
        with self.assertRaises(TypeError):
            account.receive(receiveAmount)
    
    def test_should_withdraw_an_amount_and_decrease_the_current_amount(self):
        
        initialbalance = Amount(100)

        account = BankAccount("123", initialbalance, AccountType.SAVINGS)

        withdrawamount = Amount(10)
        account.withdraw(withdrawamount)
        newbalance = account.getbalance()

        expectedbalance = (initialbalance - withdrawamount)

        self.assertEqual(newbalance, expectedbalance)
    
    def test_should_not_withdraw_an_amount_when_amount_is_invalid(self):
        
        initialbalance = Amount(100)

        account = BankAccount("123", initialbalance, AccountType.SAVINGS)

        withdrawamount = 10
        with self.assertRaises(TypeError):
            account.withdraw(withdrawamount)

    def test_should_not_withdraw_an_amount_when_the_balance_amount_is_less_that_amount(self):
        
        initialbalance = Amount(100)

        account = BankAccount("123", initialbalance, AccountType.SAVINGS)

        withdrawamount = Amount(1000000)
        with self.assertRaises(ValueError):
            account.withdraw(withdrawamount)
            
if __name__ == '__main__':
    unittest.main() 