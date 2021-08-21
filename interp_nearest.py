import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x=np.array([-1.0,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1.0])
y=np.array([0.03846,0.06639,0.13793,0.39024,1,0.39024,\
            0.13793,0.06639,0.03846])

f=interpolate.interp1d(x,y,'nearest')

xs=np.linspace(-1,1,50)
ys=f(xs)
xi=0.85
yi=f(xi)

print(yi)

plt.plot(x,y,'o',label='Datos')
plt.plot(xi,yi,'sr',label='Interpolacion')
plt.plot(xs,ys,'r:',label='Nearest')
plt.text(xi+0.05,yi, ' interpolacion ' + str(yi))
plt.title('$f(x)=1/(1+25x^2)$')
plt.legend()
plt.grid(True)
plt.show()