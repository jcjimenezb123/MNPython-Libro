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
plt.title('Regla de los Trapecios Compuesta')

# Make the shaded region
n=4
ix = np.linspace(a, b,n)
iy = func(ix)
patterns=('+','x','/','\\','O','.','o','*','\\','/','-','x','+')
for i in range(n-1):
    verts = [(ix[i], 0), (ix[i],iy[i]),(ix[i+1],iy[i+1]), (ix[i+1], 0)]
    poly = Polygon(verts,facecolor='0.9', edgecolor='0.5', hatch=patterns[i])
    ax.add_patch(poly)

#ax.text(0.5 * (a + b), 40, r"$\int_a^b p_0(x)\mathrm{d}x$",
#        horizontalalignment='center', fontsize=20)

fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a,(a+b)/2, b))
ax.set_xticklabels(('$x_0$','...', '$x_n$'))

plt.show()
fig.savefig("integral_trapM.pdf", bbox_inches='tight')