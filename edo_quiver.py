import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2.2, 0.2)
y = np.arange(0, 2.2, 0.2)

X, Y = np.meshgrid(x, y)
u = 1
v = -2 * Y


def f(x_valor):
    return np.exp(-2 * x_valor) * 1.5


fig, ax = plt.subplots()
ax.quiver(X, Y, u, v)

x = np.arange(0, 2.1, 0.01)
y = f(x)
ax.plot(x, y, 'r', label='Solución particular para $C_{A0}$')
ax.set_title('dy/dx=-2y')
ax.set_xlabel('tiempo')
ax.set_ylabel('concentración')
ax.legend()
fig.savefig("edo_quiver.jpg", bbox_inches='tight')

plt.show()
