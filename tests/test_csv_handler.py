#!/usr/bin/env python
# -*- coding:utf-8 -*-           
# @Time : 2024/6/6 16:03
# @Author  : chenJiaHui
import csv
import unittest
import os
import csv_handler


class TestCSVHandler(unittest.TestCase):

    def setUp(self):
        # 创建一个临时CSV文件用于测试
        self.filename = 'test.csv'
        data = [
            {'name': 'Alice', 'balance': 1000},
            {'name': 'Bob', 'balance': 500},
        ]
        csv_handler.save_to_csv(self.filename, data)

    def tearDown(self):
        # 测试结束后删除临时CSV文件
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load_csv(self):
        # 加载CSV文件并验证内容
        loaded_data = csv_handler.load_from_csv(self.filename)
        self.assertEqual(len(loaded_data), 2)
        self.assertEqual(loaded_data[0]['name'], 'Alice')
        self.assertEqual(loaded_data[0]['balance'], '1000')
        self.assertEqual(loaded_data[1]['name'], 'Bob')
        self.assertEqual(loaded_data[1]['balance'], '500')

    def test_load_empty_csv(self):
        # 创建一个空的CSV文件并尝试加载
        empty_filename = 'empty.csv'
        with open(empty_filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'balance'])
            writer.writeheader()

        # 加载并验证是否为空列表
        loaded_data = csv_handler.load_from_csv(empty_filename)
        self.assertEqual(len(loaded_data), 0)

        # 清理临时文件
        os.remove(empty_filename)


if __name__ == '__main__':
    unittest.main()