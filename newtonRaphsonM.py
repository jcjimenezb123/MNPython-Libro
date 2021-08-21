#importar las funciones de la biblioteca math
import numpy as np
import matplotlib.pyplot as plt
import math 
import cmath 

def newtonRaphsonM(f,df,d2f,x,imax=100,tol=1e-8):
    cumple=False
    print('{:^10s} {:^10s} {:^10s} {:^10s}'.\
          format('x','f(x)','df(x)','d2f(x)'))
    k=0
    while (not cumple and k<imax):
        x=x-(f(x)*df(x))/(df(x)**2-f(x)*d2f(x))
        print('{:10.5f} {:10.5f} {:10.5f}'.\
              format(x,f(x),df(x),d2f(x)))
        cumple=abs(f(x))<=tol
        k+=1
    if k<imax:
        return x
    else:
        raise ValueError ('La funcion no converge')

# Funcion a evaluar
def f(x):
    return (x-2)*(x-2)*(x-4)
# Derivada
def df(x):
    return (x - 4)*(2*x - 4) + (x - 2)**2
# Segunda derivada
def d2f(x):
    return 2*(3*x - 8)

def main():
    # valores iniciales
    x0=1
    # Llamada al algoritmo
    raiz=newtonRaphsonM(f,df,d2f,x0)
    print('f({:e})={:e}'.format(raiz,f(raiz)))
    
    x=np.linspace(1,5)
    y=f(x)
    
    fig = plt.figure()
    plt.plot(x,y)
    plt.title('$f(x)=(x-2)(x-2)(x-4)$')
    plt.scatter(raiz,f(raiz))
    plt.text(raiz,f(raiz),' Raiz '+str(raiz),color='red')
    plt.grid()
    
    plt.show()
    fig.savefig("newtonraphsonm.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()