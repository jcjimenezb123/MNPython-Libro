#importar las funciones de la biblioteca math
import numpy as np
import matplotlib.pyplot as plt
import math 
import cmath 

def wegstein(g,x0,imax=100,tol=1e-8):
    cumple=False
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s}'.\
          format('x1','x2','x3','g(x1)','g(x3)','g(x3)'))
    x1=g(x0)
    x2=g(x1)
    k=0
    while (not cumple and k<imax):
        x3=(x1*g(x2)-x2*g(x1))/(x1-g(x1)-x2+g(x2))
        print('{:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f}'.\
              format(x1,x2,x3,g(x1),g(x2),g(x3)))
        x1=x2        
        x2=x3
        cumple=abs(x2-g(x2))<=tol
        
        k+=1
    if k<imax:
        return x3
    else:
        raise ValueError ('La funcion no converge')

# Funcion a evaluar
def g(v):
    n=2
    R=0.082
    a=3.592
    b=0.04267
    T=300
    P=10
    return n*R*T/(P+n**2*a/v**2)+n*b

def main():
    # valores iniciales
    x0=2
    # Llamada al algoritmo
    raiz=wegstein(g,x0)
    print('f({:e})={:e}'.format(raiz,g(raiz)-raiz))
    
    x=np.linspace(0.01,6,100)
    y=g(x)-x
    
    fig = plt.figure()
    plt.plot(x,y,label='$f(x)$')
    
    plt.plot(x,x,':',label='$x$')
    plt.plot(x,g(x),':',label='$g(x)$')
    plt.plot(np.array([raiz,raiz]),np.array([0,g(raiz)]),'-.')

    plt.title('Volumne de $CO_2$')
    plt.scatter(raiz,g(raiz)-raiz)
    plt.text(raiz,g(raiz)-raiz,' Raiz '+str(raiz),color='red')
    plt.legend()
    plt.grid()
    plt.show()
    fig.savefig("wegstein.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()