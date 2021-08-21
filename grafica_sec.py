import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,3,50)

def f(x):
    return np.exp(-x)-2

y=f(x)

fig = plt.figure()
ax = plt.gca()
plt.plot(x,y)

x0=-2
x1=-1

x=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
fx=0
plt.plot(np.array([x0,x1,x]),np.array([f(x0),f(x1),0]),'o-')
#plt.plot(np.array([xx,xx]),np.array([0,f(xx)]),'o--')
plt.title('Secante')
plt.grid()

plt.text(x0,f(x0),'$f(x_0)$')
plt.text(x1,f(x1),'$f(x_1)$')

plt.text(x0,0,'$x_0$')
plt.text(x1,0,'$x_1$')


ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.show()
fig.savefig("graficasec.pdf", bbox_inches='tight')