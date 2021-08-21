import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

#cuadratura de 2 puntos
def cuadratura2(f,a,b):
    x1=(b-a)/2*(-1/np.sqrt(3))+(a+b)/2
    x2=(b-a)/2*(1/np.sqrt(3))+(a+b)/2
    r=(b-a)/2*(f(x1)+f(x2))
    return r

#funcion a integrar
def f(x):
    return 2.41+0.057195*x-4.3e-6*x**2

def grafica_cuadratura2(f,a,b):
    x = np.linspace(a, b)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'b', linewidth=1.7)
    ax.set_ylim(bottom=0)
    
    x1=(b-a)/2*(-1/np.sqrt(3))+(a+b)/2
    x2=(b-a)/2*(1/np.sqrt(3))+(a+b)/2
    
    linea=lagrange(np.array([x1,x2]),np.array([f(x1),f(x2)]))
    
    ax.plot(np.array([x1,x1]),np.array([0,f(x1)]),'--g')
    ax.plot(np.array([x2,x2]),np.array([0,f(x2)]),'--g')
    
    ax.set_ylim(bottom=0)
    plt.title('Cuadratura')
    
    patterns=('/','x','/','\\','O','.','o','*','\\','/','-','x','+')
    
    verts = [(a, 0), (a,linea(a)),(b,linea(b)), (b, 0)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.1',hatch=patterns[0])
    ax.add_patch(poly)

    plt.title('Cuadratura de Gauss-Legendre')
    fig.savefig("int_cuadratura2.pdf", bbox_inches='tight')
    return plt

def main():
    a=300+273.15 #limite inferior
    b=600+273.15 #limite superior
    area=cuadratura2(f,a,b)
    print('integral = ',area)
    g=grafica_cuadratura2(f,a,b)
    g.show()
    
if __name__ == "__main__": main()