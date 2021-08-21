import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,0.5,1,1.5,2,2.5])
y = np.array([0,20.5,31.36,36.25,30.41,28.23])
xs=np.linspace(0,3.3,100)

p=np.polyfit(x,y,2)
print(p)
fig=plt.figure()
plt.scatter(x, y,label='Datos')
plt.plot(xs, np.polyval(p,xs), ':r',label='Interpolacion cuadratica')
plt.xlabel('Tiempo')
plt.ylabel('Distancia')
plt.title('Tiro Parabolico')
plt.grid()
plt.show()
fig.savefig("regcuad.pdf", bbox_inches='tight')