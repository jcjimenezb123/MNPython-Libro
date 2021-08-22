import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([[0.05,0.55,0.65,0.75,0.9,1,1.05],\
             [395,410,380,388,400,373,405]])
z = np.array([0.1561,2.8098,1.2224,1.9834,3.3847,1.3993,4.5913])

xs=np.linspace(20,51,100)

def f(x,k,b,n):
    return k*np.exp(-b/x[1])*np.power(x[0],n)

param,_=curve_fit(f,x,z)
print(param)

X=x[0,:]
Y=x[1,:]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(10,50)
ax.scatter(X, Y, z)
ax.set_xlabel('Concentracion (gmol/l)')
ax.set_ylabel('Temperatura (K)')
ax.set_zlabel('Velocidad de reaccion')
plt.title('Velocidad de Reaccion')

X = np.arange(0,1.05,0.01)
Y = np.arange(395, 405, 1)
X, Y = np.meshgrid(X, Y)
Z=f(np.array([X,Y]),*param)
surf = ax.plot_surface(X, Y, Z,cmap=plt.cm.coolwarm,
                       linewidth=0, antialiased=False)


plt.show()
#fig.savefig("regmultiple.pdf", bbox_inches='tight')