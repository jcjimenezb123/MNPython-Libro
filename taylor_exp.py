import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x0=0
n=5

x=sp.Symbol('x')
t=sp.exp(x).series(x,x0,n).removeO()
print(t)
t=sp.lambdify(x,t,'numpy')

g=plt.figure()

xx=np.linspace(x0-4,x0+4,100)
yc=np.exp(xx)
yt=t(xx)

plt.plot(xx,yc,xx,yt)
plt.legend(['$e^x$','Serie de Taylor'])
plt.title('Serie de Taylor de $f(x)=e^x$')
plt.grid(True)

g.savefig('serieex.pdf', bbox_inches='tight')