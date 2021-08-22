import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x0=0
n=8

x=sp.Symbol('x')
t=sp.series(sp.exp(1j*x),x,x0,n).removeO()
#print(t)
t=sp.lambdify(x,t,'numpy')

yt=t(np.pi)

print(yt)
xx=np.linspace(x0-4,x0+4,100)
yc=np.exp(1j*xx)
yt=t(xx)

g=plt.figure()
plt.plot(yc.real,yc.imag,yt.real,yt.imag)

plt.legend(['$e^{ix}$','Serie de Taylor'])
plt.title('Serie de Taylor de $f(x)=e^{ix}$')
plt.grid(True)
g.savefig('serieeix.pdf', bbox_inches='tight')