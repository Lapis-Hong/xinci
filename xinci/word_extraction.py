#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/6/17
from __future__ import unicode_literals

import time
import codecs
import logging

from model import EntropyJudger
from dictionary import Dictionary
from selector import CnTextSelector
from indexer import CnTextIndexer
from utils import data_reader, get_opt


class WordExtract:

    def __init__(self,
                 corpus_file,
                 common_words_file=None,
                 min_candidate_len=2,
                 max_candidate_len=5,
                 least_cnt_threshold=5,
                 solid_rate_threshold=0.018,
                 entropy_threshold=1.92,
                 all_words=False):
        if not corpus_file:
            raise ValueError("Corpus file is empty, please specify corpus file path.")
        self._document = data_reader(corpus_file, cn_only=True)
        self._common_dic = common_words_file
        self._min_candidate_len = min_candidate_len
        self._max_candidate_len = max_candidate_len
        self._least_cnt_threshold = least_cnt_threshold
        self._solid_rate_threshold = solid_rate_threshold
        self._entropy_threshold = entropy_threshold
        self._all_words = all_words
        if not self._all_words:
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
        logging.info("Document Length: {}".format(length))
        pos_tmp = 0
        for pos, candidate in candidate_generator:
            # about how to use stopwords
            if candidate[0] in self.stopwords or candidate[-1] in self.stopwords:
                continue
            if candidate in new_word_set:
                continue
            if not self._all_words:
                if candidate in self.dictionary:
                    continue
            if judger.judge(candidate):
                new_word_set.add(candidate)
            if (pos+1) % 10000 == 0 and pos != pos_tmp:
                pos_tmp = pos
                logging.info("Process {}/{} characters in document".format(pos+1, length))
        time_elapse = time.time() - s_time
        logging.info("Time Cost: {}s".format(time_elapse))
        logging.info("Speed: {} char/s".format(length / time_elapse))
        logging.info("New word size: {}".format(len(new_word_set)))
        indexer = CnTextIndexer(self._document)
        print("发现{}个新词如下:\n@新词\t@词频\n".format(len(new_word_set)))
        for w in new_word_set:
            word_cnt = indexer.count(w)
            print('{}\t{}'.format(w, word_cnt))
        if save_file:
            logging.info("Save extract words to {}".format(save_file))
            with codecs.open(save_file, 'w', encoding='utf-8') as fo:
                for w in new_word_set:
                    word_cnt = indexer.count(w)
                    fo.write(w + '\t' + str(word_cnt) + '\n')
        return new_word_set


def extract(corpus_file,
            common_words_file=None,
            min_candidate_len=2,
            max_candidate_len=5,
            least_cnt_threshold=5,
            solid_rate_threshold=0.018,
            entropy_threshold=1.92,
            all_words=False,
            save_file=None):
    """Extract chinese words from corpus.
    Args:
        corpus_file: string, input corpus file (required)
        common_words_file: string, common words dic file [common.dic]
        min_candidate_len: int, min candidate word length [2]
        max_candidate_len: int, max candidate word length [5]
        least_cnt_threshold: int, least word count to extract [5]
        solid_rate_threshold: float, solid rate threshold [0.018]
        entropy_threshold: float, entropy threshold [1.92]
        all_words: bool, set True to extract all words mode [False]
        save_file: string, output file [None]
    Returns:
        extract words set
    Raises:
        ValueError: if corpus_file is not specified.
    """
    return WordExtract(corpus_file,
                       common_words_file=common_words_file,
                       min_candidate_len=min_candidate_len,
                       max_candidate_len=max_candidate_len,
                       least_cnt_threshold=least_cnt_threshold,
                       solid_rate_threshold=solid_rate_threshold,
                       entropy_threshold=entropy_threshold,
                       all_words=all_words).extract(save_file=save_file)


if __name__ == '__main__':
    config = get_opt()
    if config.verbose:
        level = logging.ERROR
    else:
        level = logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s-%(filename)s-%(levelname)s: %(message)s")
    extractor = WordExtract(
        corpus_file=config.corpus_file,
        common_words_file=config.common_words_file,
        min_candidate_len=config.min_candidate_len,
        max_candidate_len=config.max_candidate_len,
        least_cnt_threshold=config.least_cnt_threshold,
        solid_rate_threshold=config.solid_rate_threshold,
        entropy_threshold=config.entropy_threshold,
        all_words=config.all_words)
    extractor.extract(config.save_file)





