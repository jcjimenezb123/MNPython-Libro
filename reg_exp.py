import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([0,500,1000,1500,2000,2500,3000])
y = np.array([0.1000,0.0892,0.0776,0.0705,0.0603,0.0542,0.0471])

xs=np.linspace(0,3000,100)

def f(x,a,b):
    return a*np.exp(-b*x)

param,_=curve_fit(f,x,y,p0=[0.1,-0.0001])
print(param)

#fig=plt.figure()
plt.scatter(x, y,label='Datos')
plt.plot(xs, f(xs,*param), ':r',label='Interpolacion exponencial')
plt.xlabel('tiempo')
plt.ylabel('Concentracion')
plt.legend()
plt.title('Reaccion de $N_2O_5$')
plt.grid()
plt.show()
#fig.savefig("regexp.pdf", bbox_inches='tight')