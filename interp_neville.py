import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5])
y=np.array([1,1,2,6,24,120])
n=x.size

G=np.zeros((n,n))
xi=np.pi
yi=0
#Calcula las interpolaciones y compara sus valores
G[:,0]=y
for i in range(1,n):
    for j in range(1,i+1):
        G[i,j]=((xi-x[i-j])*G[i,j-1]-(xi-x[i])*G[i-1,j-1])/(x[i]-x[i-j])
        yi=G[i,i]
        if abs(G[i,i]-G[i-1,i-1])<1e-5:
            exit
print(G)

print(yi)

plt.plot(x,y,'o')
plt.plot(xi,yi,'sr')
plt.text(xi+0.1,yi, ' $\pi$ ! ' + str(yi))
plt.title('Factorial n!')
plt.legend(['Factorial','Interpolacion'])
plt.grid(True)
plt.show()