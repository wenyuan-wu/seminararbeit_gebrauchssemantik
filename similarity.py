#! /usr/bin/python
# -*- coding: utf-8 -*-

import gensim.models
import argparse


def get_argument_parser() -> argparse.ArgumentParser:
    """Create an argument parser with required options."""
    parser = argparse.ArgumentParser(
        description='A python script to train word2vec models.')
    parser.add_argument('-m', help='input path to model', required=True)
    parser.add_argument('-f', help='first word input', required=True)
    parser.add_argument('-s', help='second word input', required=True)
    return parser


def main():
    args = get_argument_parser().parse_args()
    model = gensim.models.Word2Vec.load(args.m)
    word_vectors = model.wv
    similarity = word_vectors.similarity(args.f, args.s)
    print('Similarity between {} and {}:\t {}'.format(args.f, args.s, similarity))


if __name__ == '__main__':
    main()
