# Creating fern-like structures(Fractals)

import matplotlib.pyplot as plt
from random import random


def t_1(x, y):
    x2 = 0.85 * x + 0.04 * y
    y2 = -0.04 * x + 0.85 * y + 1.6
    return x2, y2


def t_2(x, y):
    x2 = 0.2 * x - 0.26 * y
    y2 = 0.23 * x + 0.22 * y + 1.6
    return x2, y2


def t_3(x, y):
    x2 = -0.15 * x + 0.28 * y
    y2 = 0.26 * x + 0.24 * y + 0.44
    return x2, y2


def t_4(x, y):
    x2 = 0
    y2 = 0.16 * y
    return x2, y2


def get_index(probability):
    r = random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for pos, num in enumerate(sum_probability):
        if r < num:
            return pos
    return len(probability) - 1


def transform(x1, y1):
    transformations = [t_1, t_2, t_3, t_4]
    probabilities = [0.85, 0.07, 0.07, 0.01]
    t_index = get_index(probabilities)
    func = transformations[t_index]
    x, y = func(x1, y1)
    return x, y


def draw_fern(n):
    x, y = [0], [0]

    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform(x1, y1)
        x.append(x1)
        y.append(y1)
    return x, y


if __name__ == '__main__':
    n = int(input("Enter the number of points in the fern: "))
    x, y = draw_fern(n)

    plt.scatter(x, y, c=y, cmap=plt.cm.RdPu, edgecolors=None, s= 5)
    plt.title("Fern with {0} points".format(n))
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.savefig('{0}_points_fern_RdPu.png'.format(n))
    plt.show()
