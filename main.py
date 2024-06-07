#!/usr/bin/env python
# -*- coding:utf-8 -*-           
# @Time : 2024/6/6 16:12
# @Author  : chenJiaHui

from bank_system import BankSystem

# 初始化银行系统
bank = BankSystem()
# 创建账户
bank.create_account("Alice", 1000)
bank.create_account("Bob", 500)

# 进行账户操作

# Alice存款
bank.deposit("Alice", 200)

# Bob取款
bank.withdraw("Bob", 100)

# Alice向Bob转账
bank.transfer("Alice", "Bob", 300)

# 保存系统状态到CSV文件
bank.save_state('bank_state.csv')

# 初始化新的银行系统实例
new_bank = BankSystem()

# 从CSV文件加载系统状态
new_bank.load_state('bank_state.csv')

# 现在new_bank包含了和之前保存的bank系统相同的状态
