import unittest
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.bankingoperation.bankdeposit import BankDeposit
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountType

class TestBankDeposit(unittest.TestCase):
    
    def test_not_should_start_a_bank_deposit_when_the_receiver_is_an_invalid_account(self):

        receiver = "ibrain"
        transferamount = Amount(100)
        
        with self.assertRaises(TypeError):
            BankDeposit(receiver, transferamount)

    def test_not_should_start_a_bank_deposit_when_the_transfer_amount_is_an_invalid(self):

        balance = Amount(1000)
        receiver = BankAccount(balance, AccountType.CHECKING, 12331)
        transferamount = 100
        
        with self.assertRaises(TypeError):
            BankDeposit(receiver, transferamount)

    def test_should_deposit_a_amount_in_a_account(self):

        initialbalance = Amount(1000)
        receiver = BankAccount(initialbalance, AccountType.CHECKING, 12331)
        transferamount = Amount(100)
        
        bankdeposit = BankDeposit(receiver, transferamount)
        bankdeposit.todeposit()

        newbalance = receiver.getbalance()

        expectedbalance = (initialbalance + transferamount)

        self.assertEqual(newbalance, expectedbalance)
