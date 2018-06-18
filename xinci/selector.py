#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/17
"""This module generate all possible candidate chinese words."""
from __future__ import unicode_literals
from six.moves import xrange


class CnTextSelector:

    def __init__(self, document, min_len=2, max_len=5):
        """
        Args:
            document: String, filtered chinese corpus.
            min_len: candidate word min length.
            max_len: candidate word max length.
        """
        self._document = document
        self._max_len = max_len
        self._min_len = min_len
        self._doc_len = len(document)
        # self._pos = 0  # current index of document
        # self._cur_len = max_len  # current candidate word length

    # def _adjust_cur_len(self):
    #     self._cur_len = self._max_len if self._pos+self._max_len < self._doc_len-1 else self._doc_len-self._pos

    def generate(self):
        """Returns:
            A generator of candidate chinese word from document.
        """
        for pos in xrange(self._doc_len-self._min_len):
            for cur_len in xrange(self._min_len, self._max_len+1):
                yield pos, self._document[pos:pos+cur_len]
        # while self._pos + self._min_len <= self._doc_len - 1:  # not end
        #     if self._cur_len < self._min_len:
        #         self._pos += 1
        #         self._adjust_cur_len()
        #     self._cur_len -= 1
        #     yield self._document[self._pos:self._pos+self._cur_len+1]









