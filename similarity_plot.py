#! /usr/bin/python
# -*- coding: utf-8 -*-

import gensim.models
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


def get_similarity(model, word_1: str, word_2: list):
    model = gensim.models.Word2Vec.load(model)
    word_vectors = model.wv
    similarity_dict = {}
    for word in word_2:
        try:
            similarity = word_vectors.similarity(word_1, word)
        except KeyError:
            similarity = 0
        similarity_dict[word] = similarity
    return similarity_dict


def get_simi_dict(word, word_list):
    simi_dict = {}
    for i in range(1995, 2000):
        model_path = "models/{}-model".format(i)
        simi_dict[i] = get_similarity(model_path, word, word_list)
    for i in range(2001, 2016):
        model_path = "models/{}-model".format(i)
        simi_dict[i] = get_similarity(model_path, word, word_list)
    return simi_dict


def plot_data(simi_dict, word):
    df = pd.DataFrame.from_dict(simi_dict)
    x_year = df.columns.values.tolist()
    x = np.arange(len(x_year))
    fig, ax = plt.subplots()
    color = iter(cm.rainbow(np.linspace(0, 1, 10)))
    for idx in df.index.values.tolist():
        y = df.loc[idx].values.tolist()
        ax.plot(x, y, 'o-', color=next(color), alpha=1.0, label=idx)
    ax.grid(axis='x', color='0.95')
    for line, name in zip(ax.lines, df.index.values.tolist()):
        y = line.get_ydata()[-1]
        ax.annotate(name, xy=(1, y), xytext=(6, 0), color=line.get_color(),
                    xycoords=ax.get_yaxis_transform(), textcoords="offset points",
                    size=12, va="center")
    ax.set_ylabel('Distribution per year', size=12)
    ax.set_title('Similarity with word "{}"'.format(word), size=12)
    ax.set_xticks(x)
    ax.set_xticklabels(x_year)
    ax.legend()
    fig.tight_layout()
    plt.show()


def main():
    word_list_1995 = ['lärmschutz', 'klimaschutz', 'kahlschlag', 'polizeieinsatz', 'schulordnung',
                      'passus', 'asylkompromiß', 'kohlepfennig', 'todesstoß', 'bürgerentscheid']
    word_list_2015 = ['richtlinien', 'suchmaschinen', 'netzneutralität', 'infrastrukturen', 'provider',
                      'webseiten', 'regeln', 'transparenz', 'compliance', 'rechtliche']

    simi_dict_1995 = get_simi_dict('datenschutz', word_list_1995)
    simi_dict_2015 = get_simi_dict('datenschutz', word_list_2015)
    plot_data(simi_dict_1995, 'datenschutz')
    plot_data(simi_dict_2015, 'datenschutz')


if __name__ == '__main__':
    main()
