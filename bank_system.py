#!/usr/bin/env python
# -*- coding:utf-8 -*-           
# @Time : 2024/6/6 15:59
# @Author  : chenJiaHui
from account import Account
from csv_handler import save_to_csv, load_from_csv


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        if name not in self.accounts:
            self.accounts[name] = Account(name, initial_balance)
            print(f"Account created for {name} with initial balance: {initial_balance}")
        else:
            print(f"Account for {name} already exists.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)
        else:
            print(f"Account for {name} does not exist.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            self.accounts[name].withdraw(amount)
        else:
            print(f"Account for {name} does not exist.")

    def transfer(self, from_name, to_name, amount):
        if from_name in self.accounts and to_name in self.accounts:
            from_account = self.accounts[from_name]
            to_account = self.accounts[to_name]
            if from_account.transfer(amount, to_account):
                print(f"Transfer of {amount} from {from_name} to {to_name} successful.")
            else:
                print("Transfer failed.")
        else:
            print("One or both accounts do not exist.")

    def save_state(self, filename):
        accounts_data = [{'name': name, 'balance': account.balance} for name, account in self.accounts.items()]
        save_to_csv(accounts_data, filename)

    def load_state(self, filename):
        data = load_from_csv(filename)
        for row in data:
            self.create_account(row['name'], row['balance'])