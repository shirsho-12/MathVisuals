
from matplotlib import pyplot as plt


def draw_axes(l):
    ax = plt.axes(xlim=(0, l), ylim=(0, l))
    return ax


def draw_square(l, ax):
    square = plt.Polygon([(0, 0), (l, 0), (l, l), (0, l)], color='#114488', alpha=0.5, closed=True)
    ax.add_patch(square)


def draw_circles(r, l, ax):
    y = r
    while y < l:
        x = r
        while x < l:
            circle = plt.Circle((x, y), radius=r, color='#226688')
            ax.add_patch(circle)
            x += r * 2

        y += r * 2


if __name__ == '__main__':
    length = float(input("Enter length of square: "))
    radius = float(input("Enter radius of circles: "))
    axes = draw_axes(length)
    draw_square(length, axes)
    draw_circles(radius, length, axes)
    axes.set_aspect('equal')
    plt.show()
