import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


x = np.array([6,9,11,13,22,26,28,33,35])
y = np.array([68,67,65,53,44,40,37,34,32])

m, b, r, p, std_err = stats.linregress(x, y)

print('Ordenada al origen ', b)
print('pendiente ', m)
print('coeficiente de correlacion ', r)

y_pred = m*x+b
print('datos corregidos ', y_pred, sep='\n')

#fig=plt.figure()
plt.plot(x,y,'o',label='Datos')
plt.plot(x,y_pred,'r:',label='Regresion lineal')
plt.title('Deformacion y Dureza')
plt.xlabel('Dureza')
plt.ylabel('Deformacion')
plt.legend()
plt.grid(True)
plt.show()
#fig.savefig("reglineal.pdf", bbox_inches='tight')