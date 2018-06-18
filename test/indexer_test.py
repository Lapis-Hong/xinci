#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/18
from __future__ import unicode_literals
# import unittest

from xinci.indexer import CnTextIndexer


# class TestCnTextIndexer(unittest.TestCase):
#     pass


if __name__ == '__main__':
    # unittest.main()
    from xinci.utils import data_reader

    document = data_reader('../xinci/test.txt', cn_only=True)
    indexer = CnTextIndexer(document)
    print(indexer._char_pos_map)
    print(indexer.count('食物'))
    print(indexer.count('食'))
    print(list(indexer.find('食物')))
    print(len(list(indexer.find('食物'))))
    print(indexer[1])