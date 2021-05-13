import matplotlib.pyplot as plt

x_values = list(int(x) for x in range(-5, 5))

y_values = []
for x in x_values:
    y = x**2 + 2*x - 3
    y_values.append(y)

plt.plot(x_values, y_values, marker="o")
# plt.plot([-5,5],[0,0],color='black')
# plt.plot([0,0],[-5,21],color='black')

plt.axvline(0,color='black')
plt.axhline(0,color='black')
plt.tick_params(axis='both', which="major", labelsize=16)
plt.axis('tight')
plt.axis([-5, 5, min(y_values), max(y_values)])
plt.tick_params(direction='out')
plt.show()

