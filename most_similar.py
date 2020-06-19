#! /usr/bin/python
# -*- coding: utf-8 -*-

import gensim.models
import argparse
from gensim.similarities.index import AnnoyIndexer


def get_argument_parser() -> argparse.ArgumentParser:
    """Create an argument parser with required options."""
    parser = argparse.ArgumentParser(
        description='A python script to train word2vec models.')
    parser.add_argument('-m', help='input path to model', required=True)
    parser.add_argument('-w', help='words input', required=True)
    return parser


def main():
    args = get_argument_parser().parse_args()
    model = gensim.models.Word2Vec.load(args.m)
    annoy_index = AnnoyIndexer(model, 100)
    vector = model.wv[args.w]
    approximate_neighbors = model.wv.most_similar([vector], topn=11, indexer=annoy_index)

    print("Approximate Neighbors")
    for neighbor in approximate_neighbors:
        print("{}\t{:.4f}".format(neighbor[0], neighbor[1]))


if __name__ == '__main__':
    main()
