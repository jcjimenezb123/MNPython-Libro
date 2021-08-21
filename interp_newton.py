import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,4,8,13,18])
y=np.array([1.1,1.5,12.8,15.3,15.5])
n=x.size

t=np.zeros((n,n))
t[:,0]=y

#Genera la tabla de diferencias
for c in range(1,n):
    for r in range(0,n-c):
        t[r,c]=(t[r + 1, c-1] - t[r, c-1]) / (x[r + c ] - x[r])
print(t)

#calcula la interpolacion de xi
xi=3
xt = 1
yi = t[0, 0]
for k in range(0,n-1):
    xt = xt * (xi - x[k])
    yi = yi + t[0, k + 1] * xt

print(yi)

plt.plot(x,y,'o')
plt.plot(xi,yi,'sr')
plt.text(xi+0.1,yi, ' Profundidad ' + str(yi))
plt.title('Profundidad del agua')
plt.legend(['Datos','Interpolacion'])
plt.grid(True)
plt.show()