import unittest
from app.financemanagement.accounttype import *

class TestSavingsAccountTypeRules(unittest.TestCase):

    def test_should_not_allow_withdrawal_when_the_amount_does_exceed_the_limit_for_withdrawal(self):
        
        savingsaccounttyperule = SavingsAccountTypeRules()
        
        with self.assertRaises(ValueError):
            savingsaccounttyperule.checklimitwithdrawal(Amount(3400))

    def test_should_not_allow_withdrawal_when_the_amount_does_exceed_the_limit_for_receive(self):
        
        savingsaccounttyperule = SavingsAccountTypeRules()
        
        with self.assertRaises(ValueError):
            savingsaccounttyperule.checklimitreceive(Amount(6000))

class TestCheckingAccountTypeRules(unittest.TestCase):

    def test_should_not_allow_withdrawal_when_the_amount_does_exceed_the_limit_for_withdrawal(self):
        
        checkingaccounttyperules = CheckingAccountTypeRules()
        
        with self.assertRaises(ValueError):
            checkingaccounttyperules.checklimitwithdrawal(Amount(8000))

    def test_should_not_allow_withdrawal_when_the_amount_does_exceed_the_limit_for_receive(self):
        
        checkingaccounttyperules = CheckingAccountTypeRules()
        
        with self.assertRaises(ValueError):
            checkingaccounttyperules.checklimitreceive(Amount(10000))
    

class TestAccountTypeRulesFactory(unittest.TestCase):

    def test_not_should_make_a_account_type_rules_for_a_type_invalid(self):
        
        accounttyperulesfactory = AccountTypeRulesFactory()

        with self.assertRaises(TypeError):
            accounttyperulesfactory.make(33)

    def test_should_make_a_savings_account_type_rules_for_savings_account_type(self):

        accounttyperulesfactory = AccountTypeRulesFactory()

        savingsaccounttyperules = accounttyperulesfactory.make(AccountType.SAVINGS)

        self.assertIsInstance(savingsaccounttyperules, SavingsAccountTypeRules)
        self.assertIsNotNone(savingsaccounttyperules)

    def test_should_make_a_checking_account_type_rules_for_checking_account_type(self):

        accounttyperulesfactory = AccountTypeRulesFactory()

        checkingsaccounttyperules = accounttyperulesfactory.make(AccountType.CHECKING)

        self.assertIsInstance(checkingsaccounttyperules, CheckingAccountTypeRules)
        self.assertIsNotNone(checkingsaccounttyperules)