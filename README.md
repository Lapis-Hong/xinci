# xinci 
## 新词发现 Chinese Words Extraction & New Words Finder (python package).


## install
### 1. using pip
```
pip install xinci
```
### 2. using setup.py
``` 
git clone git@github.com:Lapis-Hong/xinci.git  
cd xinci 
pip setup.py install
```

## Usage:

### 1. command line
```
cd xinci
python word_extraction.py 
```
or 
```
./run.sh
```

### 2. as a python package
```
>>> import xinci
# modify common word dic, add words or remove words
dic = xinci.Dictionary()
dic.add(['神马']
dic.add_from_file('user.dic')

dic.remove(['神马']
dic.remove_from_file('user.dic')

# find new words
we = xinci.WordExtract('corpus.txt')
we.extract()
```

The code is based on follow java version
https://github.com/GeorgeBourne/grid

