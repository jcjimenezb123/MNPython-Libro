import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x=np.array([4.1,12.2,20.3,28.2,38.1,45.2])
y=np.array([1.0276,1.1013,1.1801,1.2652,1.3480,1.4120])


xfino=np.linspace(4.1,45.2,100)
yi=interpolate.interp1d(x,y,kind='linear')

xi=15
yii=yi(xi)

plt.plot(x,y,'o',xfino,yi(xfino),'-',xi,yii,'sr')
plt.legend(['Datos','Interpolacion Lineal','Dato interpolado'])
plt.title('Interpolacion Lineal Carbonato de Sodio')
plt.xlabel('Concentracion')
plt.ylabel('Densidad')
plt.text(xi, yii, ' %C ' + str(xi) + ' Densidad ' + str(yii))

plt.grid(True)
plt.show()