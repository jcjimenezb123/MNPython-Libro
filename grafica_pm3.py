import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return -(x - 3) * (x - 5)  + 85


a, e, b = 2, 5, 9  # integral limits
x = np.linspace(0, 10)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'b', linewidth=1.7)

plt.plot(np.array([a,b]),np.array([func(a),func(b)]),'o')

plt.plot(np.array([a,e]),np.array([func(a),func(e)]),'o-')

#ax.set_ylim(bottom=0)
plt.title('Diferencias hacia atras')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a,e, b))
ax.set_xticklabels(('$x_{i-1}$', '$x_i$','$x_{i+1}$'))
ax.text(a-0.5, func(a)+3, '$f(x_{i-1})$')
ax.text(b, func(b)+3, '$f(x_{i+1})$')
ax.text(e, func(e)+1, '$f(x_i)$')
plt.show()
fig.savefig("grafica_bd.jpg", bbox_inches='tight')