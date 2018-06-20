#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/17
"""This module contains a Indexer class for given document. Efficient for computing word frequency."""
from __future__ import unicode_literals

import logging

from collections import defaultdict
from utils import TextUtils


class CnTextIndexer:

    def __init__(self, document):
        self._document = document
        self._doc_len = len(document)
        self._char_pos_map = defaultdict(list)
        self._char_cnt_map = defaultdict(int)
        self._init_char_mapping()

    def _init_char_mapping(self):
        """Save each character index in document in self._char_pos_map."""
        for ix, char in enumerate(self._document):
            self._char_pos_map[char].append(ix)
            self._char_cnt_map[char] += 1
        logging.info("Initialized char position mapping and char count mapping in document.")

    def count(self, target):
        """Target text count in document"""
        if not target:
            return 0

        index = self._char_pos_map[target[0]]
        if len(index) == 0:
            return 0

        if len(target) == 1:
            return len(index)

        count = 0
        for pos in index:
            if TextUtils.match(self._document, pos, target):
                count += 1

        return count

    def find(self, target):
        """All target text matching start index in document
        Yields:
            index_list
        """
        if not target:
            yield 0
        # 获取候选词的第一个字符出现在文本中的所有下标
        index = self._char_pos_map[target[0]]
        if len(index) == 0:
            yield 0

        if len(target) == 1:
            for pos in index:
                yield pos

        for pos in index:
            if TextUtils.match(self._document, pos, target):
                yield pos

    def __getitem__(self, index):
        if index < 0 or index > self._doc_len-1:
            return ""
        return self._document[index]

    @property
    def char_cnt_map(self):
        return self._char_cnt_map






