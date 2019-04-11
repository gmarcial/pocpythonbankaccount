import unittest
from app.financemanagement.bankaccount import BankAccount
from app.financemanagement.bankingoperation.banktransfer import BankTransfer
from app.financemanagement.amount import Amount
from app.financemanagement.accounttype import AccountType
from app.financemanagement.bankingoperation.bankoperationtype import BankOperationType


class TestBankTransfer(unittest.TestCase):

    def test_not_should_start_a_bank_transfer_when_the_sender_is_an_invalid_account(self):

        sender = "receiver"

        receiveramount = Amount(2000)
        receiver = BankAccount("123", receiveramount, AccountType.SAVINGS)

        transferamount = Amount(750)
        with self.assertRaises(TypeError):
            BankTransfer(sender, receiver, transferamount)

    def test_not_should_start_a_bank_transfer_when_the_receiver_is_an_invalid_account(self):

        senderamount = Amount(1000)
        sender = BankAccount("123", senderamount, AccountType.CHECKING)

        receiver = "receiver"

        transferamount = Amount(750)
        with self.assertRaises(TypeError):
            BankTransfer(sender, receiver, transferamount)

    def test_not_should_start_a_bank_transfer_when_the_transfer_amount_is_an_invalid(self):

        senderamount = Amount(1000)
        sender = BankAccount("123", senderamount, AccountType.CHECKING)

        receiveramount = Amount(2000)
        receiver = BankAccount("123", receiveramount, AccountType.SAVINGS)

        transferamount = 750
        with self.assertRaises(TypeError):
            BankTransfer(sender, receiver, transferamount)

    def test_should_transfer_a_amount_between_two_accounts(self):

        senderinitialamount = Amount(1000)
        sender = BankAccount("123", senderinitialamount, AccountType.CHECKING, 10)

        receiverinitialamount = Amount(2000)
        receiver = BankAccount("123", receiverinitialamount,
                               AccountType.SAVINGS, 12)

        transferamount = Amount(750)
        banktransfer = BankTransfer(sender, receiver, transferamount)
        transferrecord = banktransfer.transfer()

        expectedamountsender = (senderinitialamount - transferamount)
        senderbalance = sender.getbalance()

        expectedamountreceiver = (receiverinitialamount + transferamount)
        receiverbalance = receiver.getbalance()

        transferrecordsender = transferrecord[0]
        transferrecordreceiver = transferrecord[1]

        self.assertEqual(expectedamountsender, senderbalance)
        self.assertEqual(expectedamountreceiver, receiverbalance)

        self.assertEqual(transferrecordsender.getamount(), -int(transferamount))
        self.assertEqual(transferrecordsender.getoperation(), BankOperationType.TRANSFER)

        self.assertEqual(transferrecordreceiver.getamount(), int(transferamount))
        self.assertEqual(transferrecordreceiver.getoperation(), BankOperationType.TRANSFER)
