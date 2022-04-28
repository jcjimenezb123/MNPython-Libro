import numpy as np
import matplotlib.pyplot as plt

#definición del método de Newton-Raphson
def nr(f,df,x0,tol=1e-5):
    k=0
    while np.abs(f(x0))>tol and k<50:
        x0=x0-f(x0)/df(x0)
        k=k+1
    return x0,k #devuelve la raíz y las iteraciones

#define la función y su derivada
f=lambda x:x**2-2
df=lambda x:2*x

x0=-2 #valor inicial
x=np.empty(400)
y=np.empty(400)
for i in range(400):
    x[i]=x0
    _,y[i]=nr(f,df,x0)
    x0=x0+0.01 #incrementa el valor inicial
plt.plot(x,y)
plt.show()
