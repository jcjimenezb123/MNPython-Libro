from math import *
import numpy as np
import matplotlib.pyplot as plt

# Algoritmo de Biseccion
def biseccion(f, x0, x1, tol):
    if f(x0) * f(x1) > 0:
        raise ValueError ('La funcion no cambia de signo en este rango')
    
    sigue = False
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s}'.\
              format('x0','x','x1','f(x0)','f(x)','f(x1)'))
    while (not sigue):
        x = (x0 + x1) / 2
        print('{:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f}'.\
              format(x0,x,x1,f(x0),f(x),f(x1)))
        if f(x0) * f(x) < 0:
            x1 = x
        else:
            x0 = x
        sigue = abs(f(x)) < tol
    return x

# Funcion a evaluar
def f(x):
    return x**2-2

def main():
    # valores iniciales
    x0=-1.6
    x1=-1.4
    tol=1e-4
    # Llamada al algoritmo
    raiz=biseccion(f,x0,x1,tol)
    print('f({:e})={:e}'.format(raiz,f(raiz)))
    
    x=np.linspace(x0,x1,100)
    y=f(x)
    
    fig = plt.figure()
    ax = plt.gca()
    plt.plot(x,y)
    plt.scatter(raiz,f(raiz))
    plt.text(raiz,f(raiz),' Raiz '+str(raiz),color='red')
    plt.grid()
    
    plt.show()
    #fig.savefig("biseccion.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()