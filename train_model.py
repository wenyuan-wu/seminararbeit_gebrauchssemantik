#! /usr/bin/python
# -*- coding: utf-8 -*-


import multiprocessing
from gensim import utils
import gensim.models
from pathlib import Path
import time
from tqdm import tqdm


class MyCorpus(object):
    """An interator that yields sentences (lists of str)."""

    def __iter__(self):
        corpus_path = Path('data/1995.txt')
        for line in tqdm(corpus_path.open()):
            # assume there's one document per line, tokens separated by whitespace
            yield utils.simple_preprocess(line)


def main():
    start = time.process_time()
    sentences = MyCorpus()
    model = gensim.models.Word2Vec(sentences=sentences, workers=multiprocessing.cpu_count())
    print('Training finished. Time taken: {}'.format(time.process_time() - start))
    model.save('models/1995-model')


if __name__ == '__main__':
    main()
