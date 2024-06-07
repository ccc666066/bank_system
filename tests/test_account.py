#!/usr/bin/env python
# -*- coding:utf-8 -*-           
# @Time : 2024/6/6 16:01
# @Author  : chenJiaHui
import unittest
from account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("Test User", 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        self.account.withdraw(20)
        self.assertEqual(self.account.balance, 80)

    def test_withdraw_insufficient_funds(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 100)

    def test_transfer(self):
        recipient = Account("Recipient User", 0)
        self.assertTrue(self.account.transfer(50, recipient))
        self.assertEqual(self.account.balance, 50)
        self.assertEqual(recipient.balance, 50)

    def test_transfer_insufficient_funds(self):
        recipient = Account("Recipient User", 0)
        self.assertFalse(self.account.transfer(150, recipient))
        self.assertEqual(self.account.balance, 100)
        self.assertEqual(recipient.balance, 0)


if __name__ == '__main__':
    unittest.main()