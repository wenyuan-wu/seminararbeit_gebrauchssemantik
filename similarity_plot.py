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


def plot_data(simi_dict, word, ann='right'):
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
        if ann == 'left':
            y = line.get_ydata()[0]
            ax.annotate(name, xy=(0, y), xytext=(-25, 0), color=line.get_color(),
                        xycoords=ax.get_yaxis_transform(), textcoords="offset points",
                        size=12, va="center")
        elif ann == 'right':
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
    word_list_1995_d = ['lärmschutz', 'klimaschutz', 'kahlschlag', 'polizeieinsatz', 'schulordnung',
                      'passus', 'asylkompromiß', 'kohlepfennig', 'todesstoß', 'bürgerentscheid']
    word_list_2015_d = ['richtlinien', 'suchmaschinen', 'netzneutralität', 'infrastrukturen', 'provider',
                      'webseiten', 'regeln', 'transparenz', 'compliance', 'rechtliche']
    word_list_all_d = ['jugendschutz', 'datensicherheit', 'tierschutz', 'umweltschutz', 'klimaschutz',
                       'anlegerschutz', 'opferschutz', 'bürokratieabbau', 'kinderschutz', 'arbeitsrecht']
    simi_dict_1995_d = get_simi_dict('datenschutz', word_list_1995_d)
    simi_dict_2015_d = get_simi_dict('datenschutz', word_list_2015_d)
    simi_dict_all_d = get_simi_dict('datenschutz', word_list_all_d)
    plot_data(simi_dict_1995_d, 'datenschutz', ann='right')
    plot_data(simi_dict_2015_d, 'datenschutz', ann='left')
    plot_data(simi_dict_all_d, 'datenschutz', ann='right')

    word_list_1995_p = ['unversehrtheit', 'beschneidung', 'verstrickung', 'lebensumstände', 'eignung',
                        'schweigepflicht', 'einschüchterung', 'besessenheit', 'friedenspolitik', 'eigenart']
    word_list_2015_p = ['agb', 'dienste', 'webseiten', 'cookies', 'posts',
                        'postings', 'netzwerke', 'bedürfnisse', 'suchmaschinen', 'inhalte']
    word_list_all_p = ['intimsphäre', 'anonymität', 'menschenwürde', 'grundrechte', 'redefreiheit',
                       'pressefreiheit', 'freiheitsrechte', 'unversehrtheit', 'urheberrechte', 'berufsfreiheit']
    simi_dict_1995_p = get_simi_dict('privatsphäre', word_list_1995_p)
    simi_dict_2015_p = get_simi_dict('privatsphäre', word_list_2015_p)
    simi_dict_all_p = get_simi_dict('privatsphäre', word_list_all_p)
    plot_data(simi_dict_1995_p, 'privatsphäre', ann='right')
    plot_data(simi_dict_2015_p, 'privatsphäre', ann='left')
    plot_data(simi_dict_all_p, 'privatsphäre', ann='right')


if __name__ == '__main__':
    main()
