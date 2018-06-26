# xinci 新词 & 抽词
**xinci** is a Python interface for chinese words extraction & new words extraction.
[https://pypi.org/project/xinci/]
c++ version see [fast-xinci](https://github.com/Lapis-Hong/fast-xinci)

## Requirements
Python >= 2.7

## Installation
### 1. using pip
```shell
pip install xinci
```
### 2. using setup.py
``` shell
git clone https://github.com/Lapis-Hong/xinci.git 
cd xinci 
pip setup.py install
```

## Usage
This package has two main use cases: words extraction and
find new words. 

### 1. command line
```shell
cd xinci
python word_extraction.py 
```
or 
```
./run.sh
```

### 2. python package
```python 
import xinci

# if you want to see logging events.
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')

# init default dictionary or user dic,
dic = xinci.Dictionary()
# load vocab, vocab is a python set.
vocab = dic.load()  # or dic.dictionary
print(vocab)

# add words to dic
dic.add(['神马'])  # or dic.add_from_file('user.dic')
# remove words from dic
dic.remove(['神马'])  # or dic.remove_from_file('user.dic')

# extract new words, xc is a set
xc = xinci.extract('corpus.txt')
for w in xc:
    print(w)
# extract all words, c is a set
c = xinci.extract('corpus.txt', all_words=True)
for w in xc:
    print(w)
```
result
```angular2html
发现5个新词如下:
@新词	@词频
祛斑	13
后再	7
今日头条	9
洗净切	7
蛋液	9
```
### Notes: Iteratively add "not seems to new words" in result to common dic will improve a lot. 


## API documentation
```python
xc = xinci.extract(params)

```
List of available `params` and their default value:
```angular2html
corpus_file:           string, input corpus file (required)
common_words_file:     string, common words dic file [common.dic]
min_candidate_len:     int, min candidate word length [2]
max_candidate_len:     int, max candidate word length [5]
least_cnt_threshold:   int, least word count to extract [5]
solid_rate_threshold:  float, solid rate threshold [0.018]
entropy_threshold:     float, entropy threshold [1.92]
all_words: bool,       set True to extract all words mode [False]
save_file: string,     output file [None]
```

## References
The code is based on this java version
[https://github.com/GeorgeBourne/grid]

