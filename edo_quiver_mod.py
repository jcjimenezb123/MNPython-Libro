import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,0.6,0.1)
y = np.arange(0,1.5,0.2)


X, Y = np.meshgrid(x, y)
u = 1
v = -2*Y

def f(x):
    return np.exp(-2*x)*1.5

fig, ax = plt.subplots()
ax.quiver(X,Y,u,v)

m1=-2*1.5
x = np.arange(0,0.6,0.1)
y=x*m1+1.5
ax.plot(x,y,':m',label='$m_1=f(x_i,y_i)$')

m2=y[-1]
y=x*m2+m2
ax.plot(x,y,'.:b',label='$m_2=f(x_{i+1},y_{i+1})$')

m3=(m1+m2)/2
y=x*m3+1.5
ax.plot(x,y,'-r',label='$m_p=(m_1+m_2)/2$')

ax.plot(x,f(x),'g-',label='Función')

plt.legend()
plt.title('Euler modificado')
plt.xlabel('tiempo')
plt.ylabel('Concentración')
plt.show()


#fig.savefig("edo_quiver_mod3.pdf", bbox_inches='tight')
