import matplotlib.pyplot as plt


def draw_graph(x, y):
    plt.plot(x, y, marker='x')
    plt.xlabel("Distance in metres")
    plt.ylabel("Force in Newton")
    plt.title("Plot of gravitational force against distance")
    plt.show()


def gen_fr(m1 = 1000, m2 = 1000):
    r = list(range(100, 1001, 50))
    F = []
    for x in r:
        F.append((6.674*(10**-11)) * m1 * m2 / x**2)
    draw_graph(r, F)


if __name__ == '__main__':
    gen_fr()