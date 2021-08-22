import numpy as np
import math 
import cmath 

def secante(f,x0,x1,imax=100,tol=1e-8):
    cumple=False
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s}'.\
          format('x0','x1','x','f(x0)','f(x1)','f(x)'))
    k=0
    while (not cumple and k<imax):
        x=x1-f(x1)*(x0-x1)/(f(x0)-f(x1))
        print('{:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f}'.\
              format(x0,x1,x,f(x0),f(x1),f(x)))
        x0=x1
        x1=x
        cumple=abs(f(x))<tol
        k+=1
    if k<imax:
        return x
    else:
        raise ValueError ('La funcion no converge')

# Funcion a evaluar
def f(x):
    return x**2+2

def main():
    # valores iniciales
    x0=1j
    x1=2j
    # Llamada al algoritmo
    raiz=secante(f,x0,x1,100,1e-4)
    print('f({:e})={:e}'.format(raiz,f(raiz)))
        
if __name__ == "__main__": main()