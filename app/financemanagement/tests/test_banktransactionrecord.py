import unittest
from datetime import datetime
from app.financemanagement.amount import Amount
from app.financemanagement.bankingoperation.bankoperationtype import BankOperationType
from app.financemanagement.bankingoperation.banktransactionrecord import BankTransactionRecord

class TestBankTransactionRecord(unittest.TestCase):

    def test_not_should_register_a_bank_transaction_when_the_operation_is_invalid(self):

        whenoccurred = datetime.now()
        amount = 100
        description = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        
        with self.assertRaises(TypeError):
            BankTransactionRecord(13, "123", whenoccurred, amount, description, 1)

    def test_not_should_register_a_bank_transaction_when_the_date_is_invalid(self):

        whenoccurred = "10/20/2019"
        amount = 100
        description = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        
        with self.assertRaises(TypeError):
            BankTransactionRecord(BankOperationType.DEPOSIT, "123", whenoccurred, amount, description, 1)

    def test_not_should_register_a_bank_transaction_when_the_amount_is_invalid(self):

        whenoccurred = datetime.now()
        amount = Amount(100)
        description = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        
        with self.assertRaises(TypeError):
            BankTransactionRecord(BankOperationType.DEPOSIT, "123", whenoccurred, amount, description, 1)

    def test_not_should_register_a_bank_transaction_when_the_description_is_invalid_type(self):

        whenoccurred = datetime.now()
        amount = 100
        description = []
        
        with self.assertRaises(TypeError):
            BankTransactionRecord(BankOperationType.DEPOSIT, "123", whenoccurred, amount, description, 1)

    def test_not_should_register_a_bank_transaction_when_the_description_is_invalid_lenght(self):

        whenoccurred = datetime.now()
        amount = 100
        description = "AAAAAA"
        
        with self.assertRaises(ValueError):
            BankTransactionRecord(BankOperationType.DEPOSIT, "123", whenoccurred, amount, description, 1)

    def test_not_should_register_a_bank_transaction_when_the_contaid_is_invalid(self):

        whenoccurred = datetime.now()
        amount = 100
        description = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        
        with self.assertRaises(TypeError):
            BankTransactionRecord(BankOperationType.DEPOSIT, "123", whenoccurred, amount, description, -1)

    def test_should_register_a_bank_transaction(self):

        whenoccurred = datetime.now()
        amount = 100
        description = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        
        banktransactionrecord = BankTransactionRecord(BankOperationType.DEPOSIT, "123", whenoccurred, amount, description, 1)
        
        self.assertIsInstance(banktransactionrecord, BankTransactionRecord)
        self.assertIsNotNone(banktransactionrecord)