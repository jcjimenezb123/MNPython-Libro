import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

x=np.array([300,350,400,450,500])
y=np.array([150,200,250,300])
z=np.array([[3073.3,3174.7,3277.5,3381.7,3487.6],
            [3072.1,3173.8,3276.7,3381.1,3487.0],
            [3070.9,3172.8,3275.9,3380.4,3486.5],
            [3069.7,3171.9,3275.2,3379.8,3486.0]])

f=interpolate.interp2d(x,y,z,'cubic') 
zi=f(420,190)

print(zi)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(10,35)
ax.set_xlabel('Temperatura (K)')
ax.set_ylabel('Presion (kPa)')
ax.set_zlabel('Entalpia (kJ/Kg')
ax.set_title('Entalpia de vapor supercalentado')
surf=ax.plot_surface(X, Y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(3000, 3500)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.0f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
#fig.savefig("interp2d.pdf", bbox_inches='tight')