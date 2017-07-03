import os
import nltk

from nltk import regexp_tokenize
from konlpy.tag import Twitter;

t = Twitter()
import matplotlib as mp
import numpy as np

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')


def read_data_and_print():
    print("------------------")
    file = open(desktop + "/summary2.json").read()
    _get_count(file)
    print("------------------")


def _get_count(file):
    en = _analysis_en()
    print(len(en.tokens))  # returns number of tokens (document length)
    # Set에 담아 중복제거처리
    print(len(set(en.tokens)))  # returns number of unique tokens
    vocabs = en.vocab()
    vocabs.plot(50)


def _analysis_en(doc_en):
    pattern = r'''(?x) ([A-Z]\.)+ | \w+(-\w+)* | \$?\d+(\.\d+)?%? | \.\.\. | [][.,;"'?():-_`]'''
    tokens_en = regexp_tokenize(doc_en, pattern)
    en = nltk.Text(tokens_en);
    print(len(en.tokens))       # returns number of tokens (document length)
    print(len(set(en.tokens)))  # returns number of unique tokens
    en.vocab()                  # returns frequency distribution
    return en

def _analysis_ko(doc_ko):
    tokens_ko = t.morphs(doc_ko)
    ko = nltk.Text(tokens_ko)
    print(len(ko.tokens))       # returns number of tokens (document length)
    print(len(set(ko.tokens)))  # returns number of unique tokens
    ko.vocab()
    return ko
