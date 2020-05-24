#! /usr/bin/python
# -*- coding: utf-8 -*-


import logging
import gensim.downloader as api
import argparse


def get_argument_parser() -> argparse.ArgumentParser:
    """
    Create an argument parser with required options.

    Returns
    -------
    The argument parser with all arguments added.
    """
    parser = argparse.ArgumentParser(
        description='A Python script to compare the results of '
                    'classification with sparse vs. dense vectors')
    parser.add_argument('-i', help='input file', required=True)
    parser.add_argument('-b', help='base file', required=True)
    parser.add_argument('-t', help='target file', required=True)
    return parser



logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
info = api.info()

for model_name, model_data in sorted(info['models'].items()):
    print(
        '%s (%d records): %s' % (
            model_name,
            model_data.get('num_records', -1),
            model_data['description'][:40] + '...',
        )
    )
