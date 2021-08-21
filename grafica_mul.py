import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-0.6,1,50)

def f(x):
    return x**3-3*x**2+x+1

y=f(x)

fig = plt.figure()
ax = plt.gca()
plt.plot(x,y)

x0=0.1
x1=0.3
x2=0.5

d1=(f(x1)-f(x0))/(x1-x0)
d2=(f(x2)-f(x1))/(x2-x1)
d3=(d2-d1)/(x2-x0)
a=d3
b=d1-a*(x0+x1)
c=f(x0)+x0*(a*x1-d1)
den1=-b+np.sqrt(b**2-4*a*c)
den2=-b-np.sqrt(b**2-4*a*c)
if abs(den1)>abs(den2):
    x3=2*c/den1
else:
    x3=2*c/den2
xm=np.linspace(x0,x3,50)
ym=np.polyval([a,b,c],xm)

fx3=0
plt.plot(np.array([x0,x1,x2,x3]),np.array([f(x0),f(x1),f(x2),0]),'o')
plt.plot(xm,ym,'--')
plt.title('Muller')
plt.grid()

plt.text(x0,f(x0),'$f(x_0)$')
plt.text(x1,f(x1),'$f(x_1)$')
plt.text(x2,f(x2),'$f(x_2)$')

plt.text(x0,0,'$x_0$')
plt.text(x1,0,'$x_1$')
plt.text(x2,0,'$x_2$')
plt.text(x3,0,'$x_3$')

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

plt.show()
fig.savefig("graficamuller.pdf", bbox_inches='tight')