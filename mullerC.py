import numpy as np
import matplotlib.pyplot as plt
import math 
import cmath 

def muller(f,x0,x1,x2,imax=100,tol=1e-8):
    cumple=False
    print('{:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s} {:^10s}'.\
          format('x0','x1','x2','x3','f(x0)','f(x1)','f(x2)','f(x3)'))
    k=0
    while (not cumple and k<imax):
        d1=(f(x1)-f(x0))/(x1-x0)
        d2=(f(x2)-f(x1))/(x2-x1)
        d3=(d2-d1)/(x2-x0)
        a=d3
        b=d1-a*(x0+x1)
        c=f(x0)+x0*(a*x1-d1)
        den1=-b+np.sqrt(b**2-4*a*c)
        den2=-b-np.sqrt(b**2-4*a*c)
        if abs(den1)>abs(den2):
            x3=2*c/den1
        else:
            x3=2*c/den2

        print(\
              '{:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f} {:10.5f}'.\
              format(x0,x1,x2,x3,f(x0),f(x1),f(x2),f(x3)))
        x0=x1
        x1=x2
        x2=x3
        cumple=abs(f(x3))<tol
        k+=1
    if k<imax:
        return x3
    else:
        raise ValueError ('La funcion no converge')

# Funcion a evaluar
def f(x):
    return x**2+2

def main():
    # valores iniciales
    x0=0j #valor complejo para que los resultados puedan ser complejos
    x1=1
    x2=2
    # Llamada al algoritmo
    raiz=muller(f,x0,x1,x2,100,1e-4)
    print('f({:e})={:e}'.format(raiz,f(raiz)))
    
if __name__ == "__main__": main()