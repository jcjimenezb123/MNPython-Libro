import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([20,22,25,27,30,34,40,43,48,51])
y = np.array([1.175,1.230,1.312,1.365,1.443,\
              1.544,1.690,1.761,1.875,1.942])

xs=np.linspace(20,51,100)

def f(x,a,b,c):
    return a+b/(x+c)

param,_=curve_fit(f,x,y)
print(param)

#fig=plt.figure()
plt.scatter(x, y,label='Datos')
plt.plot(xs, f(xs,*param), ':r',label='Regresion')
plt.xlabel('Temperatura')
plt.ylabel('Log(P)')
plt.legend()
plt.title('Presion de Vapor de la sacarosa')
plt.grid()
plt.show()
#fig.savefig("regAntoine.pdf", bbox_inches='tight')