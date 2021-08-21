import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import matplotlib 

def fx(x):
    return 1/(1+25*x**2)

x=np.array([-1.0,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1.0])
y=np.array([0.03846,0.06639,0.13793,0.39024,1,0.39024,\
            0.13793,0.06639,0.03846])

xs=np.linspace(-1,1,100)

f=interpolate.lagrange(x,y)
ys=f(xs)

g=plt.figure()
plt.plot(xs,ys,'-',label='Lagrange')
ys=fx(xs)
plt.plot(xs,ys,'-',label='f(x)')

plt.plot(x,y,'o',label='Datos')
plt.title('$f(x)=1/(1+25x^2)$')
plt.legend()
plt.grid(True)


plt.show()

g.savefig('ProbRunge.png', bbox_inches='tight',transparent=True)