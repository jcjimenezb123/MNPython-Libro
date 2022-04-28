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
f=lambda x:x**8+15*x**4-16
df=lambda x:8*x**7+60*x**3

re = np.linspace(-2, 2, 500) #rango de valores reales
im = np.linspace(-2, 2, 500) #rango de valores imaginarios

its=[]
datos = np.empty((len(re), len(im)))
for i in range(len(re)):
        for j in range(len(im)):
            x0=complex(re[i], im[j]) #crear el número complejo
            _,it = nr(f,df,x0) #corre el método y obtiene las iteraciones
            datos[i,j]=it #guarda el numero de iteraciones en el arreglo

#grafica el arreglo    
plt.imshow(datos.T, interpolation="spline36", cmap='turbo')
plt.axis('off')
plt.show()