import numpy as np
from scipy import interpolate
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x=np.array([4.1,12.2,20.3,28.2,38.1,45.2])
y=np.array([1.0276,1.1013,1.1801,1.2652,1.3480,1.4120])


xfino=np.linspace(4.1,45.2,100)
yi=interpolate.interp1d(x,y,kind='linear')


def f(x,a,b):
    return a+b*x

popt,=curve_fit(f,x,y)
yr=f(x,*popt)

plt.plot(x,y,'o',xfino,yi(xfino),'-',x,yr,'--')
plt.legend(['Datos','Interpolacion Lineal','Regresion Lineal'])
plt.title('Interpolacion Lineal vs Regresion Lineal')
plt.grid(True)