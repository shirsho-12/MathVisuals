# Circle in a square. Darts thrown.
# Area of circle is the product of area of square times the ratio of darts fallen in the circle.

from random import uniform
from math import pi, sqrt


def estimate(radius, num):
    num_in_circle = 0
    for i in range(num):
        y = uniform(-r, r)
        x = uniform(-r, r)
        diagonal = sqrt(abs(y) ** 2 + abs(x) ** 2)
        if diagonal <= r:
            num_in_circle += 1
    # print(num_in_circle)
    area = (num_in_circle / num) * ((2*r) ** 2)
    print("\nEstimated value of pi({1} darts): {0}".format(4 * num_in_circle / num, num))
    return area


def actual(radius):
    return pi * radius**2


if __name__ == '__main__':
    r = float(input("Radius: "))
    nums = [1000, 100000, 1000000, 10000000]
    for number in nums:
        print("Area: {0}, Estimated ({1} darts): {2}".format(actual(r), number, estimate(r, number)))
    print("\nActual value of pi = ", pi)