import unittest
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.bankingoperation.bankdraft import BankDraft
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountType
from app.financemanagement.bankingoperation.bankoperationtype import BankOperationType


class TestBankDraft(unittest.TestCase):

    def test_not_should_start_a_bank_draft_when_the_target_is_an_invalid_account(self):

        target = "Hype"
        transferamount = Amount(100)

        with self.assertRaises(TypeError):
            BankDraft(target, transferamount)

    def test_not_should_start_a_bank_draft_when_the_transfer_amount_is_an_invalid(self):

        balance = Amount(1000)
        target = BankAccount(balance, AccountType.SAVINGS, 1231)
        transferamount = 100

        with self.assertRaises(TypeError):
            BankDraft(target, transferamount)

    def test_should_to_withdraw_a_amount_in_a_account(self):

        initialbalance = Amount(1000)
        target = BankAccount(initialbalance, AccountType.SAVINGS, 1231)
        transferamount = Amount(100)

        bankdraft = BankDraft(target, transferamount)
        withdrawrecord = bankdraft.towithdraw()

        newbalance = target.getbalance()

        expectedbalance = (initialbalance - transferamount)

        self.assertEqual(newbalance, expectedbalance)
        self.assertEqual(withdrawrecord.getamount(), -int(transferamount))
        self.assertEqual(withdrawrecord.getoperation(), BankOperationType.WITHDRAW)
