
import matplotlib.pyplot as plt
import random


def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image


def color_points():
    x_p, y_p = 800, 800
    max_iter = 50
    image = initialize_image(x_p, y_p)
    for i in range(y_p):
        for k in range(x_p):
            z = 0 + 0j
            j = 1j
            c = (-2.5 + i * 3.5 / 800) + (-1+ k * 2 / 800) * j
            z = z ** 2 + c
            iteration = 1
            while iteration < max_iter:
                if z.real * z.real + z.imag * z.imag < 4:
                    z = z ** 2 + c
                    iteration += 1
                else:
                    break
            image[k][i] = iteration/400
    plt.imshow(image, origin='lower', extent=(-2.5, 1.0, -1.0, 1.0), cmap=plt.cm.twilight_shifted, interpolation='nearest')
    plt.colorbar()
    plt.title("Mandelbrot set with {0} iterations".format(max_iter))
    plt.savefig("mandelbrot_{0}_iter".format(max_iter))
    plt.show()

"""
def nums(x, y):
    z = 0 + 0j
    c = x + y*j
    z = z**2 + c
    max_iter = 1000
    iteration = 1
    while iteration < max_iter:
        if abs(z) < 2 and iteration< :
"""
        



if __name__ == '__main__':
    color_points()