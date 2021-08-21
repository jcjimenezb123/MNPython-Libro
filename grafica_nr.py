import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,2,20)
y=np.exp(-x)-2

fig = plt.figure()
ax = plt.gca()
plt.plot(x,y)

x0=-2
fx0=np.exp(-x0)-2
dfx0=-np.exp(-x0)
xx=x0-fx0/dfx0
fx=0
plt.plot(np.array([x0,xx]),np.array([fx0,fx]),'o-')
plt.plot(np.array([xx,xx]),np.array([0,np.exp(-xx)-2]),'o--')
plt.title('Newton-Raphson')
plt.grid()

plt.text(x0,fx0,'$f(x_0)$')
plt.text(xx+0.1,fx,'x')


ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.show()
fig.savefig("graficanr.pdf", bbox_inches='tight')