#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/19
import xinci

# if you want to see logging events.
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')

# init default dictionary or user dic,
dic = xinci.Dictionary()
# load vocab, vocab is a python set.
vocab = dic.load()  # or dic.dictionary
# print(vocab)

# add words to dic
dic.add(['lll'])  # or dic.add_from_file('user.dic')
# remove words from dic
dic.remove(['lll'])  # or dic.remove_from_file('user.dic')

# extract new words, xc is a set
xc = xinci.extract('../xinci/test.txt')
for w in xc:
    print(w)

# extract all words, c is a set
c = xinci.extract('test.txt', all_words=True)
for w in xc:
    print(w)
