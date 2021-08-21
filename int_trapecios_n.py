import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def regla_trapecios(f,a,b,n):
    h=(b-a)/n
    xs=np.linspace(a,b,n+1)
    ys=f(xs)
    r=h*(ys[0]+2*sum(ys[1:n])+ys[n])/2
    return r

#funcion a integrar
def f(x):
    return np.exp(x**2)

def grafica_trapecios(f,a,b,n):
    x = np.linspace(a, b)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'b', linewidth=1.7)
    ax.set_ylim(bottom=0)
    
    ix = np.linspace(a, b,n+1)
    iy = f(ix)
    patterns=('/','x','/','\\','O','.','o','*','\\','/','-','x','+')
    for i in range(1,n):
        verts = [(ix[i], 0), (ix[i],iy[i]),(ix[i+1],iy[i+1]), (ix[i+1], 0)]
        poly = Polygon(verts, facecolor='0.9', edgecolor='0.5',hatch=patterns[i])
        ax.add_patch(poly)
    
    plt.title('Regla de los Trapecios $e^{x^2}$')
    #fig.savefig("integral_T_ex2_10.pdf", bbox_inches='tight')
    return plt

def main():
    a=0 #limite inferior
    b=1 #limite superior
    m=range(2,51,1)
    area=np.array([regla_trapecios(f,a,b,n) for n in m])
    print('integral = ',area)
    
    fig = plt.figure()
    plt.plot(m,area,':',label='Integral')
    plt.title('Regla de los Trapecios')
    plt.xlabel='n'
    plt.ylabel='Integral'
    plt.legend()
    plt.grid()
    plt.show()
    fig.savefig("integral_trap_n.pdf", bbox_inches='tight')
    #g=grafica_trapecios(f,a,b,n)
    #g.show()
    
if __name__ == "__main__": main()