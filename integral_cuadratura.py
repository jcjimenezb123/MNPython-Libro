import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return -(x - 3) * (x - 5)  + 75

def x2_(a,b):
    return (b-a)/2*(1/np.sqrt(3))+(a+b)/2

def x1_(a,b):
    return (b-a)/2*(-1/np.sqrt(3))+(a+b)/2

a, b = 2, 9  # integral limits
x = np.linspace(0, 10)
y = func(x)
x1=x1_(a,b)
x2=x2_(a,b)
fig, ax = plt.subplots()
ax.plot(x, y, 'b', linewidth=1.7)

ax.plot(np.array([x1,x1]),np.array([0,func(x1)]),'--g')
ax.plot(np.array([x2,x2]),np.array([0,func(x2)]),'--g')

ax.set_ylim(bottom=0)
plt.title('Cuadratura')

# Make the shaded region
patterns=('/','x','/','\\','O','.','o','*','\\','/','-','x','+')

verts = [(a, 0), (a,func(x1)+(b-a)/2),(b,func(x2)-(b-a)/2), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.1',hatch=patterns[0])
ax.add_patch(poly)

fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a,x1,x2, b))
ax.set_xticklabels(('$a$','$x_1$', '$x_2$', '$b$'))
ax.text(x1, func(x1)+3, '$f(x_1)$')
ax.text(x2, func(x2)+3, '$f(x_2)$')

ax.set_yticks([])

plt.show()
fig.savefig("integral_cuadratura.pdf", bbox_inches='tight')