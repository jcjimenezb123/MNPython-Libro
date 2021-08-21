import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    #return -(x - 3) * (x - 5)*(-x+3)  + 85
    return np.sin(x/2)+2


a, b = 2, 9  # integral limits

x = np.linspace(0, 9.5)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'b', linewidth=1.7)
ax.set_ylim(bottom=0)
plt.title('Regla de Simpson 1/3')

# Make the shaded region
patterns=('|','/','\\','O','.','o','*','\\','/','-','x','+')
ix = np.linspace(a, (a+b)/2)
pol=lagrange(np.array([a,(a+b)/2,b]),
             np.array([func(a),func((a+b)/2),func(b)]))
iy=pol(ix)
verts = [(a, 0), *zip(ix,iy), ((a+b)/2, 0)]
poly = Polygon(verts,facecolor='0.9', edgecolor='0.5',hatch=patterns[1])
ax.add_patch(poly)

ix = np.linspace((a+b)/2,b)
pol=lagrange(np.array([a,(a+b)/2,b]),
             np.array([func(a),func((a+b)/2),func(b)]))
iy=pol(ix)
verts = [((a+b)/2, 0), *zip(ix,iy), (b, 0)]
poly = Polygon(verts,facecolor='0.9', edgecolor='0.5', hatch=patterns[1])
ax.add_patch(poly)

ax.text(0.5 * (a + b), 1, r"$\int_a^b p_2(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)

fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a,(a+b)/2, b))
ax.set_xticklabels(('$a$','$(a+b)/2$', '$b$'))
ax.text(a, func(a), '$f(a)$')
ax.text((a+b)/2, func((a+b)/2), '$f((a+b)/2$')
ax.text(b, func(b), '$f(b)$')
ax.set_yticks([])

plt.show()
fig.savefig("integral_simp13_.pdf", bbox_inches='tight')