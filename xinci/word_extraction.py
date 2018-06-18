#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/17
from __future__ import unicode_literals

import os
import time
import codecs
import logging

from model import EntropyJudger
from dictionary import Dictionary
from selector import CnTextSelector
from indexer import CnTextIndexer
from utils import data_reader, get_opt


logger = logging.getLogger(__name__)


class WordExtract:

    def __init__(self,
                 corpus_file,
                 common_words_file=None,
                 min_candidate_len=2,
                 max_candidate_len=5,
                 least_cnt_threshold=5,
                 solid_rate_threshold=0.018,
                 entropy_threshold=1.92,
                 new_words=True):
        if not corpus_file:
            raise ValueError("Corpus file is empty, please specify corpus file path.")
        self._document = data_reader(corpus_file, cn_only=True)
        self._common_dic = common_words_file or os.path.join(os.getcwd(), 'common.dic')
        self._min_candidate_len = min_candidate_len
        self._max_candidate_len = max_candidate_len
        self._least_cnt_threshold = least_cnt_threshold
        self._solid_rate_threshold = solid_rate_threshold
        self._entropy_threshold = entropy_threshold
        self._new_words = new_words
        if self._new_words:
            self.dictionary = Dictionary(self._common_dic)
        else:
            logging.warning("Extract all words mode, if you only want new words, set new_words=False to new words mode.")

    stopwords = {'我', '你', '您', '他', '她', '谁', '哪', '那', '这',
                 '的', '了', '着', '也', '是', '有', '不', '在', '与',
                 '呢', '啊', '呀', '吧', '嗯', '哦', '哈', '呐'}

    def extract(self, save_file=None):
        """New word discover is based on statistic and entropy, better to sure
        document size is in 100kb level, or you may get a unsatisfied result.
        """
        s_time = time.time()
        length = len(self._document)
        new_word_set = set()
        selector = CnTextSelector(self._document, self._min_candidate_len, self._max_candidate_len)
        judger = EntropyJudger(self._document, self._least_cnt_threshold, self._solid_rate_threshold, self._entropy_threshold)
        candidate_generator = selector.generate()
        logger.info("Document Length: {}".format(length))
        pos_tmp = 0
        for pos, candidate in candidate_generator:
            # about how to use stopwords
            if candidate[0] in self.stopwords or candidate[-1] in self.stopwords:
                continue
            if candidate in new_word_set:
                continue
            if self._new_words:
                if candidate in self.dictionary:
                    continue
            if judger.judge(candidate):
                new_word_set.add(candidate)
            if (pos+1) % 10000 == 0 and pos != pos_tmp:
                pos_tmp = pos
                logger.info("Process {}/{} characters in document".format(pos+1, length))
        time_elapse = time.time() - s_time
        logger.info("Time Cost: {}s".format(time_elapse))
        logger.info("Speed: {} char/s".format(length / time_elapse))
        logger.info("New word size: {}".format(len(new_word_set)))
        if save_file:
            logger.info("Save extract words to {}".format(save_file))
            indexer = CnTextIndexer(self._document)
            with codecs.open(save_file, 'w', encoding='utf-8') as fo:
                for w in new_word_set:
                    word_cnt = indexer.count(w)
                    logger.info('{}\t{}'.format(w, word_cnt))
                    fo.write(w + '\t' + str(word_cnt) + '\n')
        return new_word_set


if __name__ == '__main__':
    config = get_opt()
    if config.verbose:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=logging.INFO)
    extractor = WordExtract(
        corpus_file=config.corpus_file,
        common_words_file=config.common_words_file,
        min_candidate_len=config.min_candidate_len,
        max_candidate_len=config.max_candidate_len,
        least_cnt_threshold=config.least_cnt_threshold,
        solid_rate_threshold=config.solid_rate_threshold,
        entropy_threshold=config.entropy_threshold,
        new_words=config.new_words)
    extractor.extract(config.save_file)





