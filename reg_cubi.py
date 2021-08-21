import numpy as np
import matplotlib.pyplot as plt

x = np.array([50,100,150,200,273.16,298.15,300,400,500,600,\
               700,800,900,1000,1100,1200,1300,1400,1500])
y = np.array([34.06,41.3,48.79,56.07,68.74,73.6,73.93,94.01,\
              112.59,128.7,142.67,154.77,163.35,174.6,182.67,\
              189.74,195.85,201.21,205.89])

xs=np.linspace(50,1500,100)

p=np.polyfit(x,y,3)
print(p)
#fig=plt.figure()
plt.scatter(x, y,label='Datos')
plt.plot(xs, np.polyval(p,xs), ':r',label='Interpolacion cubica')
plt.xlabel('Temperatura')
plt.ylabel('Cp')
plt.legend()
plt.title('Cp del Propano')
plt.grid()
plt.show()
#fig.savefig("regcubi.pdf", bbox_inches='tight')