import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([5,40,70,100])
y = np.array([0.2322,0.6450,0.820,0.9856])

xs=np.linspace(0,100,100)

def f(x,a,b):
    return a*np.power(x,b)

param,_=curve_fit(f,x,y)
print(param)

#fig=plt.figure()
plt.scatter(x, y,label='Datos')
plt.plot(xs, f(xs,*param), ':r',label='Interpolacion Potencial')
plt.xlabel('altura')
plt.ylabel('Flujo')
plt.legend()
plt.title('Flujo del tanque')
plt.grid()
plt.show()
#fig.savefig("regpot.pdf", bbox_inches='tight')