#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/18
from __future__ import unicode_literals
# import unittest

from xinci.model import EntropyJudger


# class TestEntropyJudger(unittest.TestCase):
#     pass


if __name__ == '__main__':
    # unittest.main()
    from xinci.utils import data_reader
    document = data_reader('../xinci/test.txt', cn_only=True)
    jugder = EntropyJudger(document)
    print(jugder._get_entropy('食物'))
    print(jugder._get_solid_rate('食物'))
    print(jugder.judge('食物'))
