#!/usr/bin/env python3

from data import DATA

from itertools import islice

from matplotlib import pyplot as plt
from numpy import arange


def draw(ax, title, data, width, gap, cm, font_color, color_offset=0):
    labels = [label for label, _ in data.items()]
    sizes = [size for _, size in data.items()]

    ax.axis('equal')
    ax.set_axis_off()

    if title:
        ax.set(title=title)

    colormap = plt.get_cmap(cm)
    colors = colormap(arange(color_offset, len(data) + color_offset))

    pie, labels = ax.pie(
        sizes,
        colors=colors,
        labels=labels,
        radius=1,
        textprops=dict(color=font_color),
    )
    plt.setp(pie, width=width, edgecolor='white', linewidth=gap)

    for label in labels:
        if label.get_text() != 'others':
            label.set_fontfamily('monospace')


def build_all_data(data, special):
    new_data = dict()

    for name in special:
        count = data.get(name, 0)

        if count > 0:
            new_data[name] = count

    others_count = sum((count for name, count in data.items() if name not in special))

    if others_count > 0:
        new_data['others'] = others_count

    return new_data


def build_others_data(data, excluded, highlighted):
    for name in excluded:
        data.pop(name, None)

    sorted_data = sorted(data.items(), key=lambda item: item[1], reverse=True)

    special = islice(sorted_data, highlighted)

    others = islice(sorted_data, highlighted, None)
    others_count = sum((count for _, count in others))

    new_data = {k: v for k, v in special}

    if others_count > 0:
        new_data['others'] = others_count

    return new_data


def main():
    width = 0.4
    gap = 4
    cm = 'Set2'
    font_color = '0.4'
    special = [
        'root',
        'admin',
    ]
    excluded = [
        'root',
    ]

    fig, ax = plt.subplots(1, 2)

    # More space between subplots to fit labels.
    plt.subplots_adjust(wspace=0.5)

    data = build_all_data(DATA, special)
    draw(ax[0], "all usernames", data, width, gap, cm, font_color)

    data = build_others_data(DATA, excluded, 6)
    draw(ax[1], "without root", data, width, gap, cm, font_color, len(excluded))

    plt.show()


if __name__ == "__main__":
    main()
