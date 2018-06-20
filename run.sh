#!/usr/bin/env bash

# The script run the xinci program.
# Usage:
#		1. bash run.sh  $corpus_file                 # use default common words dic
#       2. bash run.sh  $corpus_file $user_dic_file  # pass 2nd argument to load user common words dic
set -e

show_usage() {
    echo 'Usage: bash run.sh $corpus_file [$user_dic_file]'
}



cd xinci

if [ $# == 0 ]; then
    show_usage
elif [ $# == 1 ]; then
    python word_extraction.py -f $1
elif [ $# == 2 ]; then
    python word_extraction.py -f $1 -d $2
fi

