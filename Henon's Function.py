
import matplotlib.pyplot as plt
from matplotlib import animation


def move(x, y):
    x_1 = y + 1 - 1.4 * (x ** 2)
    y_1 = 0.3 * x
    return x_1, y_1


def draw_point(i, arr_x, arr_y):    # Same variable name has to be used for the arrays in both functions
    x = arr_x[i]
    y = arr_y[i]
    point = plt.plot([x], [y], marker='o', color='b')
    return x, y


def plot(x, y, num):
    arr_x, arr_y = [x], [y]
    for i in range(num):
        x_new, y_new = move(arr_x[i], arr_y[i])
        arr_x.append(x_new)
        arr_y.append(y_new)
    # print(arr_x, arr_y)
    
    plt.axes(xlim=(min(arr_x),max(arr_x)), ylim=(min(arr_y), max(arr_y)))

    # print(min(arr_x), max(arr_x), min(arr_y), max(arr_y))
    # plt.scatter(arr_x, arr_y, c=arr_y, cmap=plt.cm.pink_r, edgecolors=None, s=5)

    fig = plt.gcf()
    plt.gca()
    anim = animation.FuncAnimation(fig, draw_point, fargs=(arr_x, arr_y), frames=len(arr_x), interval=1)
    plt.title("Henon's curve with {0} points".format(num))
    plt.show()


if __name__ == '__main__':
    nums = int(input("Enter number of points: "))
    plot(0, 0, nums)
