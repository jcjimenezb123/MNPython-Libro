import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x0=1
n=5

x=sp.Symbol('x')
t=sp.log(x).series(x,x0,n).removeO()
print(t)
t=sp.lambdify(x,t,'numpy')

g=plt.figure()

xx=np.linspace(x0-0.9,x0+2,100)
yc=np.log(xx)
yt=t(xx)

plt.plot(xx,yc,xx,yt)
plt.legend(['ln(x)','Serie de Taylor orden 4'])
plt.title('Serie de Taylor de $f(x)=ln(x)$')
plt.grid(True)

g.savefig('serieln.pdf', bbox_inches='tight')