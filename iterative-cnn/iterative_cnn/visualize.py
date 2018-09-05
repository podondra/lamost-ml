import matplotlib.pyplot as plt
import pandas as pd


def plot_2d_projection(title, x, y, labels):
    ax = plt.axes(title=title, xticks=[], yticks=[])
    for label in labels.unique():
        index = labels == label
        ax.plot(x[index], y[index], '.', label=label, alpha=0.5)
    ax.legend()
    return ax
