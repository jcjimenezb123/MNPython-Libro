import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def regla_rectangulos(f,a,b,n):
    h=(b-a)/n
    xs=np.linspace(a,b,n+1)
    ys=f(xs)
    r=h*sum(ys[:n])
    return r

#funcion a integrar
def f(x):
    return np.exp(x**2)

def grafica_rectangulos(f,a,b,n):
    x = np.linspace(a, b)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'b', linewidth=1.7)
    ax.set_ylim(bottom=0)
    
    ix = np.linspace(a, b,n+1)
    iy = f(ix)
    patterns=('/','x','/','\\','O','.','o','*','\\','/','-','x','+')
    for i in range(n):
        verts = [(ix[i], 0), (ix[i],iy[i]),(ix[i+1],iy[i]), (ix[i+1], 0)]
        poly = Polygon(verts, facecolor='0.9', edgecolor='0.5',hatch=patterns[i])
        ax.add_patch(poly)
    
    plt.title('Regla de los rectangulos $e^{x^2}$')
    fig.savefig("integral_ex2_10.pdf", bbox_inches='tight')
    return plt

def main():
    a=0 #limite inferior
    b=1 #limite superior
    n=10 #numero de rectangulos
    area=regla_rectangulos(f,a,b,n)
    print('integral = ',area)
    g=grafica_rectangulos(f,a,b,n)
    g.show()
    
if __name__ == "__main__": main()