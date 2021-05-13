import matplotlib.pyplot as plt
from matplotlib import animation
from math import sin, cos, radians


def plot(x, y):
    plt.plot(x, y)
    plt.xlabel("Horizontal displacement")
    plt.ylabel("Vertical displacement")
    plt.title("Trajectory of ball")
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.axis([0, x[-1], 0, None])
    plt.show()


def get_input():
    u = float(input("Enter initial velocity: "))
    theta = radians(float(input("Enter initial angle: ")))
    t_flight = (2 * u * sin(theta))/9.81
    create_animation(u, theta, t_flight)


def f_range(final, x=0, y=0.01):
    nums = []
    while final >= x:
        nums.append(x)
        x += y
    return nums


def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    x = u * t * cos(theta)
    y = u * (sin(theta) * t) - (0.5 * 9.81 * t * t)
    circle.center = x, y
    return circle


def create_animation(u, theta, t_flight):
    times = f_range(t_flight)

    x_min, x_max = 0, u * cos(theta) * times[-1]
    t_max = u * sin(theta)/9.81
    y_min, y_max = 0, u * sin(theta) * t_max - 0.5 * 9.81 * t_max ** 2
    fig = plt.gcf()
    ax = plt.axes(xlim=(x_min, x_max), ylim=(y_min, y_max))

    circle = plt.Circle((0, 0), 1.0)
    ax.add_patch(circle)
    # ax.set_aspect('equal')
    anim = animation.FuncAnimation(fig, update_position, fargs=(circle, times, u, theta),
                                   frames=len(times), interval=1, repeat=False
                                   )
    plt.title('Projectile motion')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


if __name__ == '__main__':
    get_input()
