#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/18
from __future__ import unicode_literals
import logging
import cProfile

from xinci.word_extraction import WordExtract

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    new_word_finder = WordExtract('../xinci/test.txt', '../xinci/common.dic')
    new_word_finder.extract('../result.txt')
    cProfile.run('new_word_finder.extract()')
