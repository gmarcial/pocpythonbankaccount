import unittest
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.bankingoperation.banktransfer import BankTransfer
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountType

class TestBankTransfer(unittest.TestCase):

    def test_not_should_start_a_bank_transfer_when_the_sender_is_an_invalid_account(self):

        sender = "receiver"

        receiveramount = Amount(2000)
        receiver = BankAccount(receiveramount, AccountType.SAVINGS, 6213)

        transferamount = Amount(750)
        with self.assertRaises(TypeError):
            BankTransfer(sender, receiver, transferamount)
    
    def test_not_should_start_a_bank_transfer_when_the_receiver_is_an_invalid_account(self):

        senderamount = Amount(1000)
        sender = BankAccount(senderamount, AccountType.CHECKING, 1231)

        receiver = "receiver"

        transferamount = Amount(750)
        with self.assertRaises(TypeError):
            BankTransfer(sender, receiver, transferamount)

    def test_not_should_start_a_bank_transfer_when_the_transfer_amount_is_an_invalid(self):

        senderamount = Amount(1000)
        sender = BankAccount(senderamount, AccountType.CHECKING, 1231)

        receiveramount = Amount(2000)
        receiver = BankAccount(receiveramount, AccountType.SAVINGS, 6213)

        transferamount = 750
        with self.assertRaises(TypeError):
            BankTransfer(sender, receiver, transferamount)

    def test_should_transfer_a_amount_between_two_accounts(self):
        
        senderinitialamount = Amount(1000)
        sender = BankAccount(senderinitialamount, AccountType.CHECKING, 1231)

        receiverinitialamount = Amount(2000)
        receiver = BankAccount(receiverinitialamount, AccountType.SAVINGS, 6213)

        transferamount = Amount(750)
        banktransfer = BankTransfer(sender, receiver, transferamount)
        banktransfer.transfer()

        expectedamountsender = (senderinitialamount - transferamount)
        senderbalance = sender.getbalance()
        
        expectedamountreceiver = (receiverinitialamount + transferamount)
        receiverbalance = receiver.getbalance()

        self.assertEqual(expectedamountsender, senderbalance)
        self.assertEqual(expectedamountreceiver, receiverbalance)