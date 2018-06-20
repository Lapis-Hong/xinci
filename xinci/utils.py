#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/17
"""This module contains some utility functions and classes."""
from __future__ import unicode_literals

import codecs
import re
import logging

import argparse
from six.moves import xrange

ch = logging.StreamHandler()

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


class WordCountDict(dict):

    def add(self, word):
        self[word] = self.get(word) + 1

    def get(self, word):  # override dict.get method
        return super(WordCountDict, self).get(word, 0)

    def count(self):
        return sum(self.values())


def data_reader(filename, cn_only=False):
    try:
        with codecs.open(filename, encoding='utf-8') as f:
            text = f.read()
    except UnicodeDecodeError:
        with codecs.open(filename, encoding='gbk') as f:
            text = f.read()
    if cn_only:
        # filter only chinese characters.
        re_non_cn = re.compile('[^\u4e00-\u9fa5]+')
        text = re_non_cn.sub('', text)
    return text


class TextUtils:

    @staticmethod
    def is_chinese(char):
        return u'\u4e00' <= char <= u'\u9fa5'

    @staticmethod
    def is_english(char):
        return char.isalpha()

    @staticmethod
    def is_numeric(char):
        return char.isdigit()

    @staticmethod
    def match(src, off, dest):
        src_len = len(src)
        dest_len = len(dest)
        for i in xrange(dest_len):
            if src_len <= off + i:
                return False
            if src[off+i] != dest[i]:
                return False
        return True


def get_opt():
    parser = argparse.ArgumentParser(description='Xinci.')
    parser.add_argument('-f', '--corpus_file', type=str, help='Required, input corpus file path to xinci.')
    parser.add_argument('-d', '--common_words_file', type=str, help='Optional, common words file path. ')
    parser.add_argument('--min_candidate_len', type=int, default=2, help='Candidate word min length.')
    parser.add_argument('--max_candidate_len', type=int, default=5, help='Candidate word max length.')
    parser.add_argument('--least_cnt_threshold', type=int, default=5, help='Least word count.')
    parser.add_argument('--solid_rate_threshold', type=float, default=0.018, help='Solid rate threshold.')
    parser.add_argument('--entropy_threshold', type=float, default=1.92, help='Entropy.')
    parser.add_argument('-o', '--save_file', type=str, help='New words output path.')
    parser.add_argument('-a', '--all_words', action='store_true', help='Set to extract all words.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose.')  # if -v, means True
    args, unparsed = parser.parse_known_args()
    if args.verbose:
        print "verbosity turned on"
    return args


def get_logger():
    """Return a logger instance. """
    logger = logging.getLogger("xinci")
    # logging.basicConfig(format="%(asctime)s-%(name)s-%(levelname)s: %(message)s", level=logging.INFO)  # root logger
    formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
