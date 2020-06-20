#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


x_year = list(range(1995, 2000)) + list(range(2001, 2016))
y_a = [239, 184, 194, 171, 164, 252, 202, 172, 162, 186, 211, 354, 722, 741, 630, 463, 685, 600, 1471, 1115]
y_b = [50, 44, 70, 67, 66, 59, 67, 76, 68, 64, 89, 116, 122, 103, 193, 157, 180, 243, 499, 322]

x = np.arange(len(x_year))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, y_a, width, label='Datenschutz')
rects2 = ax.bar(x + width/2, y_b, width, label='Privatsphäre')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of counts')
ax.set_title('Distribution per year')
ax.set_xticks(x)
ax.set_xticklabels(x_year)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
# plt.savefig('plot.png')
