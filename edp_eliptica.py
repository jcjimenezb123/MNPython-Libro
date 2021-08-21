import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon



a, b = 2, 9  # integral limits
c, d = 2, 7  # integral limits

fig, ax = plt.subplots()
ax.set_ylim(bottom=0)
plt.title('Region R')

# Make the shaded region
patterns=('/','+','/','\\','O','.','o','*','\\','/','-','x','+')
verts = [(a, c), (b, c),(b,d),(a,d)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5',hatch=patterns[1])
ax.add_patch(poly)

#ax.text((a + b)/2, (c+d)/2, "$R$",
#        horizontalalignment='center', fontsize=20)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks((c,d))
ax.set_yticklabels(('$c$', '$d$'))

plt.show()
fig.savefig("edp_eliptica.pdf", bbox_inches='tight')