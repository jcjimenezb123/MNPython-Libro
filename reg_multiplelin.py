import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([[15,16,24,13,21,16,22,18,20,16],\
             [70,65,71,64,84,86,72,84,71,75]])
z = np.array([156,157,177,145,197,184,172,187,157,169])

def f(x,a,b,c):
    return a+b*x[0]+c*x[1]

param,_=curve_fit(f,x,z)
print(param)

X=x[0,:]
Y=x[1,:]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(15,60)
ax.scatter(X, Y, z)
ax.set_xlabel('Temperatura')
ax.set_ylabel('Humedad')
ax.set_zlabel('Crecimiento')
plt.title('Crecimiento de paracitos')

X = np.arange(13,24,0.5)
Y = np.arange(60, 85, 0.5)
X, Y = np.meshgrid(X, Y)
Z=f(np.array([X,Y]),*param)
surf = ax.plot_surface(X, Y, Z,cmap=plt.cm.coolwarm,
                       linewidth=0, antialiased=False)


plt.show()
#fig.savefig("regmultiplelin.pdf", bbox_inches='tight')