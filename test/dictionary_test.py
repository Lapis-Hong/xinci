#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/18
import unittest
import logging

from xinci.dictionary import Dictionary


class TestDictionary(unittest.TestCase):
    pass

if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)  # 设置日志级别
    dic = Dictionary()
    for w in dic:
        print(w)
    print(len(dic))
    print('不可' in dic)
    # dic.remove(['ddd'])
    # dic.remove_from_file('user.dic')
