#! /usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing
from gensim import utils
import gensim.models
import time
from tqdm import tqdm
import argparse


class MyCorpus(object):
    """An iterator that yields sentences (lists of str)."""
    def __init__(self, infile):
        self.infile = infile

    def __iter__(self):
        with open(self.infile) as sent:
            for line in tqdm(sent):
                # assume there's one document per line, tokens separated by whitespace
                yield utils.simple_preprocess(line)


def plot_model(model, out_v, out_m):
    """generate vec and meta data to plot on tensorflow"""
    word_vectors = model.wv
    out_v = open(out_v, 'w', encoding='utf-8')
    out_m = open(out_m, 'w', encoding='utf-8')
    # Write meta file and vector file
    for index in range(len(word_vectors.index2word)):
        word = word_vectors.index2word[index]
        vec = word_vectors.vectors[index]
        out_m.write(word + "\n")
        out_v.write('\t'.join([str(x) for x in vec]) + "\n")
    out_v.close()
    out_m.close()


def get_argument_parser() -> argparse.ArgumentParser:
    """Create an argument parser with required options."""
    parser = argparse.ArgumentParser(
        description='A python script to train word2vec models.')
    parser.add_argument('-i', help='input path to corpus', required=True)
    parser.add_argument('-o', help='output path to model', required=True)
    return parser


def main():
    args = get_argument_parser().parse_args()
    start = time.process_time()
    sentences = MyCorpus(args.i)
    model = gensim.models.Word2Vec(sentences=sentences, workers=multiprocessing.cpu_count())
    out_v = args.o + '-vecs.tsv'
    out_m = args.o + '-meta.tsv'
    plot_model(model, out_v, out_m)
    print('Training corpus {} finished. Time taken: {}'.format(args.i, (time.process_time() - start)))
    model.save(args.o)


if __name__ == '__main__':
    main()
