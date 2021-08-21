import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,2,20)
y=np.exp(-x)-2

fig = plt.figure()
ax = plt.gca()
plt.plot(x,y)

x0=-2
x1=1
fx0=np.exp(-x0)-2
fx1=np.exp(-x1)-2
xx=(x0*fx1-x1*fx0)/(fx1-fx0)
fx=0
plt.plot(np.array([x0,xx,x1]),np.array([fx0,fx,fx1]),'o-')
plt.plot(np.array([xx,xx]),np.array([0,np.exp(-xx)-2]),'o--')
plt.title('Regla Falsa')
plt.grid()

plt.text(x0,fx0,'$f(x_0)$')
plt.text(xx,fx,'Falsa Raiz')
plt.text(x1,fx1,'$f(x_1)$')


ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.show()
fig.savefig("graficarf.pdf", bbox_inches='tight')