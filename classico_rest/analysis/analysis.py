import os
from nltk import regexp_tokenize
import nltk
import matplotlib as mp
import numpy as np

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')


def read_data_and_print():
    print("------------------")
    file = open(desktop + "/summary2.json").read()
    _get_count(file)
    print("------------------")


def _get_count(file):
    pattern = r'''(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\. | [][.,;"'?():-_`]'''
    tokens_en = regexp_tokenize(file, pattern)
    en = nltk.Text(tokens_en);
    #
    print(len(en.tokens))  # returns number of tokens (document length)
    # Set에 담아 중복제거처리
    print(len(set(en.tokens)))  # returns number of unique tokens
    vocabs = en.vocab()
    vocabs.plot(50)
