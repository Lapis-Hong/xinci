#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/18
"""Automated tests for checking various utils functions."""
import unittest

from xinci.utils import data_reader, TextUtils, WordCountDict


class TestUtils(unittest.TestCase):
    def test_word_count_dict(self):
        dic = WordCountDict({'a': 1, 'b': 2, 'c': 3})
        dic.add('a')
        self.assertEquals(dic['a'], 2)
        self.assertEquals(dic.get('d'), 0)
        self.assertEquals(dic.count(), 7)

    def test_data_reader(self):
        pass

    def test_text_utils(self):
        self.assertTrue(TextUtils.is_chinese('中'))
        self.assertTrue(TextUtils.is_english('a'))
        self.assertTrue(TextUtils.is_numeric('1'))
        self.assertTrue(TextUtils.match('abcde', 1, 'bc'))

if __name__ == '__main__':
    unittest.main()



