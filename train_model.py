#! /usr/bin/python
# -*- coding: utf-8 -*-


import multiprocessing
from gensim import utils
import gensim.models
from pathlib import Path


class MyCorpus(object):
    """An interator that yields sentences (lists of str)."""

    def __iter__(self):
        corpus_path = Path('data/corpus.txt')
        for line in corpus_path.open():
            # assume there's one document per line, tokens separated by whitespace
            yield utils.simple_preprocess(line)


def main():
    sentences = MyCorpus()
    model = gensim.models.Word2Vec(sentences=sentences, workers=multiprocessing.cpu_count())
    print('Done!')
    model.save('models/corpus-model')


if __name__ == '__main__':
    main()
