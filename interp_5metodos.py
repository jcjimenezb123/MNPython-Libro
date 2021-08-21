import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x=np.array([-1.0,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1.0])
y=np.array([0.03846,0.06639,0.13793,0.39024,1,0.39024,\
            0.13793,0.06639,0.03846])
tipos = ('nearest', 'zero', 'linear', 'slinear', 'quadratic', 'cubic')

xs=np.linspace(-1,1,50)

for tipo in tipos:
    f=interpolate.interp1d(x,y,kind=tipo)
    ys=f(xs)
    plt.plot(xs,ys,'-',label=tipo)

plt.plot(x,y,'o',label='Datos')
plt.title('$f(x)=1/(1+25x^2)$')
plt.legend()
plt.grid(True)
plt.show()