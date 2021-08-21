import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return -(x - 3) * (x - 5)  + 85


x_2, x_1, xi,x1,x2 = 1,3, 5, 7,9  # integral limits
x = np.linspace(0, 10)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'b', linewidth=1.7)
plt.plot(np.array([x_2, x_1, xi,x1,x2]),np.array([func(x_2),func(x_1),func(xi),func(x1),func(x2)]),'o')
plt.plot(np.array([xi,x2]),np.array([func(xi),func(x2)]),'o-')

#plt.plot(np.array([a,b]),np.array([func(a),func(b)]),'o-')

#ax.set_ylim(bottom=0)
plt.title('Diferencia de 2do Orden hacia adelante')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((x_2,x_1,xi,x1,x2))
ax.set_xticklabels(('$x_{i-2}$', '$x_{i-1}$','$x_{i}$','$x_{i+1}$','$x_{i+2}$'))
ax.text(x_2-0.7, func(x_2)+2, '$f(x_{i-2})$')
ax.text(x_1, func(x_1)+2, '$f(x_{i-1})$')
ax.text(xi, func(xi)+1, '$f(x_{i})$')
ax.text(x1, func(x1)+1, '$f(x_{i+1})$')
ax.text(x2, func(x2)+1, '$f(x_{i+2})$')
plt.show()
fig.savefig("grafica_2fd.jpg", bbox_inches='tight')