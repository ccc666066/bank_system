#!/usr/bin/env python
# -*- coding:utf-8 -*-           
# @Time : 2024/6/6 15:59
# @Author  : chenJiaHui
import csv


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'balance'])
        writer.writeheader()
        writer.writerows(data)


def load_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]