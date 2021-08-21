import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return -(x - 3) * (x - 5)  + 85


a, b = 2, 9  # integral limits
x = np.linspace(0, 10)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'b', linewidth=1.7)
ax.set_ylim(bottom=0)
plt.title('Regla de los Trapecios')

# Make the shaded region
patterns=('/','x','/','\\','O','.','o','*','\\','/','-','x','+')
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), (a,func(a)),(b,func(b)), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5',hatch=patterns[0])
ax.add_patch(poly)

fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.text(a-0.5, func(a)+3, '$f(a)$')
ax.text(b+0.3, func(b)+1, '$f(b)$')
ax.set_yticks([])

plt.show()
fig.savefig("integral_cuadratura_trap.pdf", bbox_inches='tight')