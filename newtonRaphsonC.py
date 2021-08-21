#importar las funciones de la biblioteca math
import numpy as np
import math 
import cmath 

def newtonRaphson(f,df,x,imax=100,tol=1e-8):
    cumple=False
    print('{:^10s} {:^10s} {:^10s}'.\
          format('x','f(x)','df(x)'))
    k=0
    while (not cumple and k<imax):
        if df(x)!=0:
            x=x-f(x)/df(x)
        else:
            x=x+tol
        print('{:10.5f} {:10.5f} {:10.5f}'.\
              format(x,f(x),df(x)))
        cumple=abs(f(x))<=tol
        k+=1
    if k<imax:
        return x
    else:
        raise ValueError ('La funcion no converge')

# Funcion a evaluar
def f(x):
    return x**2+2
# Derivada
def df(x):
    return 2*x

def main():
    # valores iniciales
    x0=1j
    # Llamada al algoritmo
    raiz=newtonRaphson(f,df,x0)
    print('f({:e})={:e}'.format(raiz,f(raiz)))
    
if __name__ == "__main__": main()