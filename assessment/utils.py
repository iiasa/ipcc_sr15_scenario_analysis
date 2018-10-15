#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auxiliary plotting functions for the notebooks
of the IPCC SR15 scenario assessment

@author: huppmann
"""
import numpy as np
import matplotlib.pyplot as plt
import pyam
rc = pyam.run_control()


def boxplot_by_cat(df, categories, column, years, mincount=7,
                   ymax=None, ymin=None, title=None, ylabel=None, xlabel=None,
                   legend=True, log_scale=False, hlines=None,
                   add_marker=None, ar5_format=False, save=False):

    groupby = df.groupby(column)
    _cats = len(categories) - 1
    w = 0.6 / _cats

    if add_marker is not None:
        def marker_args(m):
            return dict(zorder=3,
                        edgecolors=rc['edgecolors']['marker'][m],
                        c=rc['c']['marker'][m],
                        marker=rc['marker']['marker'][m],
                        linewidths=1)

    for i, name in enumerate(categories):
        if name not in groupby.groups or groupby.get_group(name).empty:
            continue

        _df = groupby.get_group(name)
        c = rc['color'][column][name]

        for j, y in enumerate(years):
            lst = _df[y][~np.isnan(_df[y])]
            pos = (0.75 / _cats * (i - _cats / 2) + j)

            outliers = len(lst[lst > ymax])
            if outliers > 0:
                plt.text(pos - 0.01 * len(years),
                         ymax * (1.15 if log_scale else 1.02), outliers)

            if len(lst) >= mincount:
                p = plt.boxplot(lst, positions=[pos], widths=w * .90,
                                whis=0 if ar5_format else 'range', sym='',
                                patch_artist=True)
                plt.tick_params(
                    axis='x',          # changes apply to the x-axis
                    which='both',      # both major and minor ticks are
                    bottom=False,      # ticks along the bottom edge are off
                    top=False,         # ticks along the top edge are off
                    labelbottom=True if len(years) > 1 else False)
                plt.setp(p['boxes'], color=c)
                plt.setp(p['medians'], color='black')

                if ar5_format:
                    lst = _df[y][~np.isnan(_df[y])]
                    h = max(lst) - min(lst)
                    b = min(lst)
                    plt.bar(x=pos, height=h, bottom=b, zorder=2, width=w,
                            color='white', edgecolor='grey', linewidth=0.5,
                            label=None)
                    plt.scatter(x=[pos] * len(lst), y=lst, zorder=3,
                                c='grey', edgecolors='grey', linewidth=0.5,
                                marker='x', s=15, label=None)
            else:
                plt.scatter(x=[pos] * len(lst), y=lst, zorder=6,
                            c=c, edgecolors='black', marker='o',
                            s=30, label=None)
                plt.plot([pos, pos], [max(lst), min(lst)], zorder=4,
                         color='black', linewidth=1, linestyle='-',
                         marker='_', markersize=8, markeredgewidth=1,
                         markeredgecolor='black')

            if add_marker is not None:
                for m in [i for i in _df.marker if isinstance(i, str)]:
                    _df_m = _df[_df.marker == m]
                    val = _df_m[y]
                    plt.scatter(x=pos, y=val, **marker_args(m),
                                s=50, label=None)

        plt.plot([], c=c, label='{} [{}]'.format(name, len(_df)))

    if add_marker is not None:
        for m in add_marker:
            plt.scatter(x=[], y=[], **marker_args(m), s=60, label=m)
        if ar5_format:
            plt.scatter(x=[], y=[], c='grey', edgecolors='grey', linewidth=0.5,
                        marker='x', s=15, label='other scenarios')

    if hlines is not None:
        plt.hlines(hlines, xmin=-1, xmax=len(years), colors=[(0.8, 0.8, 0.8)],
                   linewidths=0.8)

    if legend:
        plt.legend()
    if title is not None:
        plt.title(title)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    if log_scale:
        plt.yscale('log')
    plt.xlim(-0.6, (len(years) - 0.4))
    if ymax or ymin:
        plt.ylim(ymax=ymax, ymin=ymin)
    plt.xticks(range(0, len(years)), years)

    if save:
        plt.savefig(save)
