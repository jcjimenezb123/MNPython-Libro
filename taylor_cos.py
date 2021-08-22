import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x0=0
n=7

x=sp.Symbol('x')
t=sp.cos(x).series(x,x0,n).removeO()
print(t)
t=sp.lambdify(x,t,'numpy')

#g=plt.figure()

xx=np.linspace(x0-5,x0+5,1000)
yc=np.cos(xx)
yt=t(xx)

plt.plot(xx,yc,xx,yt)
plt.legend(['cos(x)','Serie de Taylor orden 7'])
plt.title('Serie de Taylor de $f(x)=cos(x)$')
plt.grid(True)

#g.savefig('seriet.pdf', bbox_inches='tight')