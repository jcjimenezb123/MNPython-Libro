import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,50)

def f(x):
    return np.cos(x)

def g(x):
    return np.power(x,2)

fig = plt.figure()
ax = plt.gca()

x0=8.241432e-01
fx0=f(x0)

plt.plot(x,f(x)-g(x),'-',label='$cos(x)-x^2$')
plt.plot(x,f(x),':',label='$cos(x)$')
plt.plot(x,g(x),':',label='$x^2$')
plt.plot(np.array([x0,x0]),np.array([0,fx0]),'-.')

plt.title('Intersección de $cos(x)$ y $x^2$')
plt.legend()
plt.grid()

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.show()
fig.savefig("graficapfijo.pdf", bbox_inches='tight')