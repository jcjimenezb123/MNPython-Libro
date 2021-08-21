import numpy as np
from scipy.interpolate import lagrange
from scipy.integrate import simps
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def regla_simpson13(f,a,b,n):
    h=(b-a)/n
    xs=np.linspace(a,b,n+1)
    ys=f(xs)
    r=h*(ys[0]+4*sum(ys[1:n:2])+2*sum(ys[2:n-1:2])+ys[n])/3
    return r

#funcion a integrar
def f(x):
    return (9+4*np.cos(0.4*x)**2)*(5*np.exp(-0.5*x)+2*np.exp(0.15*x))

def grafica_simpson(f,a,b,n):
    x = np.linspace(a, b)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'b', linewidth=1.7)
    ax.set_ylim(bottom=0)
    
    h=(b-a)/n
    x0,x1,x2=a,a+h,a+2*h
    i=0
    patterns=('-','/','\\','O','.','o','*','\\','/','-','x','+')
    for i in range(0,n,2):
        xx=np.array([x0,x1,x2])
        yy=np.array([f(x0),f(x1),f(x2)])
        pol=lagrange(xx,yy)
        
        ix = np.linspace(x0,x1)
        iy = pol(ix)
        verts = [(x0, 0), *zip(ix,iy),(x1, 0)]
        poly = Polygon(verts,facecolor='0.9', edgecolor='0.5', hatch=patterns[i])
        ax.add_patch(poly)
        
        ix = np.linspace(x1,x2)
        iy = pol(ix)
        verts = [(x1, 0), *zip(ix,iy),(x2, 0)]
        poly = Polygon(verts,facecolor='0.9', edgecolor='0.5', hatch=patterns[i])
        ax.add_patch(poly)
        
        x0,x1,x2=x2,x2+h,x2+2*h
    
    plt.title('Regla de Simpson 1/3')
    #fig.savefig("int_simpson13C.pdf", bbox_inches='tight')
    return plt

def main():
    a=2 #limite inferior
    b=8 #limite superior
    n=6 #numero de subintervalos DEBE SER MULTIPLO DE 2
    area=regla_simpson13(f,a,b,n)
    print('integral = ',area)
    
    g=grafica_simpson(f,a,b,n)
    g.show()
    
if __name__ == "__main__": main()