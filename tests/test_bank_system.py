#!/usr/bin/env python
# -*- coding:utf-8 -*-           
# @Time : 2024/6/6 16:01
# @Author  : chenJiaHui
import unittest
from bank_system import BankSystem


class TestBankSystem(unittest.TestCase):
    def setUp(self):
        self.bank = BankSystem()
        self.bank.create_account("Alice", 1000)
        self.bank.create_account("Bob", 500)

    def test_deposit(self):
        self.bank.deposit("Alice", 200)
        self.assertEqual(self.bank.accounts["Alice"].balance, 1200)

    def test_withdraw(self):
        self.bank.withdraw("Bob", 100)
        self.assertEqual(self.bank.accounts["Bob"].balance, 400)

    def test_transfer(self):
        self.bank.transfer("Alice", "Bob", 300)
        self.assertEqual(self.bank.accounts["Alice"].balance, 900)
        self.assertEqual(self.bank.accounts["Bob"].balance, 700)

    def test_save_and_load_state(self):
        filename = 'state.csv'
        self.bank.save_state(filename)
        self.bank = BankSystem()
        self.bank.load_state(filename)
        self.assertEqual(self.bank.accounts["Alice"].balance, 900)
        self.assertEqual(self.bank.accounts["Bob"].balance, 700)


if __name__ == '__main__':
    unittest.main()