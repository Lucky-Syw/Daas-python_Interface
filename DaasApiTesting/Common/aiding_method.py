# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 9:05 AM
# @Author  : Hui
# @File    : aiding_method.py

from faker import Faker
f = Faker(locale='zh_CN')
def method_faker(arg):
    if arg == "name":
        return f.name()
    if arg == 'address':
        return f.address()
    if arg == 'str_address':
        return f.street_address()
    if arg == "ssn":
        return f.ssn()
    if arg == 'company_prefix':
        return f.company_prefix()
    if arg == 'credit_card_number':
        return f.credit_card_number()
    if arg == "phone_number":
        return f.phone_number()
    if arg == 'numerify':
        return f.numerify()
    if arg == 'random_digit':
        return f.random_digit()
    else:
        pass