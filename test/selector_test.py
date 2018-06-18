#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/18
# import unittest

from xinci.selector import CnTextSelector


# class TestCnTextSelector(unittest.TestCase):
#     pass


if __name__ == '__main__':
    # unittest.main()
    from xinci.utils import data_reader
    document = data_reader('../xinci/test.txt', cn_only=True)
    selector = CnTextSelector(document)
    generator = selector.generate()

    for w in generator:
        print(w)