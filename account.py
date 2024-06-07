#!/usr/bin/env python
# -*- coding:utf-8 -*-           
# @Time : 2024/6/6 15:58
# @Author  : chenJiaHui


class Account:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.name}'s account. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.name}'s account. New balance: {self.balance}")
        else:
            print("Withdrawal failed. Insufficient funds or invalid amount.")

    def transfer(self, amount, recipient):
        if amount > 0:
            if self.withdraw(amount):
                recipient.deposit(amount)
                return True
        return False