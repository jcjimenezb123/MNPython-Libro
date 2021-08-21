import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-0.5,1.5,50)

def g(x):
    return np.exp(-x**2)

fig = plt.figure()
ax = plt.gca()

x0=0.3
x1=g(x0)
x2=g(x1)
x3=(x1*g(x2)-x2*g(x1))/(x1-g(x1)-x2+g(x2))

plt.plot(x,x,':',label='$x$')
plt.plot(x,g(x),':',label='$g(x)$')
plt.plot(np.array([x0,x0,x1,x1,x3,x0]),np.array([0,g(x0),x1,g(x1),g(x3),g(x0)]),'o--')
plt.text(x0,g(x0),'$x_1$')
plt.text(x1,g(x1),'$x_2$')
plt.text(x3,g(x3),'$x_3$')

plt.title('Metodo de Wegstein')
plt.legend()
plt.grid()

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.show()
fig.savefig("graficaw.pdf", bbox_inches='tight')