import numpy as np
import matplotlib.pyplot as plt
import math 
import cmath 

def secante(f,x0,x1,imax=100,tol=1e-8):
    cumple=False
    print('{:^10s} {:^10s} {:^10s}'.\
          format('x0','x1','x','f(x0)','f(x1)','f(x)'))
    k=0
    while (not cumple and k<imax):
        x=x1-f(x1)*(x0-x1)/(f(x0)-f(x1))
        print('{:10.5f} {:10.5f} {:10.5f}'.\
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
def f(v):
    R=0.158
    Pc=4600
    Tc=191
    a=0.427*R**2*Tc**(2.5)/Pc
    b=0.0866*Tc/Pc
    p=6000
    T=270
    return R*T/(v-b)-a/(v*(v+b)*np.sqrt(T))-p

def main():
    # valores iniciales
    x0=0.006
    x1=0.007
    # Llamada al algoritmo
    raiz=secante(f,x0,x1,100,1e-4)
    print('f({:e})={:e}'.format(raiz,f(raiz)))
    
    x=np.linspace(0.005,0.02,100)
    y=f(x)
    
    fig = plt.figure()
    plt.plot(x,y)
    plt.title('Volumen de Metano')
    plt.scatter(raiz,f(raiz))
    plt.text(raiz,f(raiz),' Raiz '+str(raiz),color='red')
    plt.grid()
    
    plt.show()
    fig.savefig("secante.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()