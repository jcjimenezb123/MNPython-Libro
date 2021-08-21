import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    #return -(x - 3) * (x - 5)*(-x+3)  + 85
    return np.sin(x/2)+2


a, b = 2, 9  # integral limits

x = np.linspace(0, 9.5,200)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'b', linewidth=1.7)
ax.set_ylim(bottom=0)
plt.title('Regla de Simpson 1/3 compuesta')

# Make the shaded region

n=6
h=(b-a)/n
x0,x1,x2,x3=a,a+h,a+2*h,a+3*h
i=0
patterns=('-','/','\\','.','.','o','*','\\','/','-','x','+')
for i in range(0,n,3):
    xx=np.array([x0,x1,x2,x3])
    yy=np.array([func(x0),func(x1),func(x2),func(x3)])
    pol=lagrange(xx,yy)
    
    ix = np.linspace(x0,x1)
    iy = pol(ix)
    verts = [(x0, 0), *zip(ix,iy),(x1, 0)]
    poly = Polygon(verts,facecolor='0.9', edgecolor='0.5', hatch=patterns[i])
    ax.add_patch(poly)
    
    ix = np.linspace(x1,x2)
    iy = pol(ix)
    verts = [(x1, 0), *zip(ix,iy),(x2, 0)]
    poly = Polygon(verts,facecolor='0.9', edgecolor='0.5', hatch=patterns[i])
    ax.add_patch(poly)
    
    ix = np.linspace(x2,x3)
    iy = pol(ix)
    verts = [(x2, 0), *zip(ix,iy),(x3, 0)]
    poly = Polygon(verts,facecolor='0.9', edgecolor='0.5', hatch=patterns[i])
    ax.add_patch(poly)
    
    x0,x1,x2,x3=x3,x3+h,x3+2*h,x3+3*h

fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a,(a+b)/2, b))
ax.set_xticklabels(('$x_0$','$...$', '$x_n$'))
ax.set_yticks([])

plt.show()
fig.savefig("integral_simp38C.pdf", bbox_inches='tight')