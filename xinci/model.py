#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/17
"""This module contains the main algorithm for chinese word extraction.
criterion 1:
    solid rate
criterion 2:
    character entropy 
"""
from __future__ import unicode_literals
from __future__ import division

import math
from indexer import CnTextIndexer
from utils import WordCountDict


class EntropyJudger:
    """Use entropy and solid rate to judge whether a candidate is a chinese word or not."""

    def __init__(self, document, least_cnt_threshold=5, solid_rate_threshold=0.018, entropy_threshold=1.92):
        """
        Args:
            least_cnt_threshold: a word least appeared count, can not pass judge if less than this value.
            solid_rate_threshold: p(candidate)/p(candidate[0]) * p(candidate)/p(candidate[1]) * ...
            entropy_threshold: min(left_char_entropy, right_char_entropy), The smaller this values is, 
                more new words you will get, but with less accuracy.
        """
        self._least_cnt_threshold = least_cnt_threshold
        self._solid_rate_threshold = solid_rate_threshold
        self._entropy_threshold = entropy_threshold
        self._indexer = CnTextIndexer(document)

    def judge(self, candidate):
        solid_rate = self._get_solid_rate(candidate)
        entropy = self._get_entropy(candidate)
        if solid_rate < self._solid_rate_threshold or entropy < self._entropy_threshold:
            return False
        return True

    def _get_solid_rate(self, candidate):
        if len(candidate) < 2:
            return 1.0
        cnt = self._indexer.count(candidate)  # candidate count in document
        if cnt < self._least_cnt_threshold:  # least count to be a word
            return 0.0
        rate = 1.0
        for c in candidate:
            rate *= cnt / self._indexer.char_cnt_map[c]  # candidate character count in document
        return math.pow(rate, 1/float(len(candidate))) * math.sqrt(len(candidate))  # interesting

    def _get_entropy(self, candidate):
        left_char_dic = WordCountDict()
        right_char_dic = WordCountDict()
        candidate_pos_generator = self._indexer.find(candidate)
        for pos in candidate_pos_generator:
            c = self._indexer[pos-1]
            left_char_dic.add(c)
            c = self._indexer[pos+len(candidate)]
            right_char_dic.add(c)

        previous_total_char_cnt = left_char_dic.count()
        next_total_char_cnt = right_char_dic.count()
        previous_entropy = 0.0
        next_entropy = 0.0
        for char, count in left_char_dic.items():  # efficient
            prob = count / previous_total_char_cnt
            previous_entropy -= prob * math.log(prob)
        for char, count in right_char_dic.items():
            prob = count / next_total_char_cnt
            next_entropy -= prob * math.log(prob)
        return min(previous_entropy, next_entropy)  # 返回前后信息熵中较小的一个




