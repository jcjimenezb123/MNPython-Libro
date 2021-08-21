#importar las funciones de la biblioteca math
import numpy as np
import matplotlib.pyplot as plt
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
    e=0.0015
    D=4
    Re=13743
    return 1/np.sqrt(x)+2*np.log10(e/D/3.7+2.51/Re/np.sqrt(x))
# Derivada
def df(x):
    e=0.0015
    D=4
    Re=13743
    return -1/(2*x**(3/2)) - \
            2.51/(Re*x**(3/2)* (2.51/(Re*np.sqrt(x)) + e/D/2.51))

def main():
    # valores iniciales
    x0=0.01
    # Llamada al algoritmo
    raiz=newtonRaphson(f,df,x0)
    print('f({:e})={:e}'.format(raiz,f(raiz)))
    
    x=np.linspace(0.0001,0.05,100)
    y=f(x)
    
    fig = plt.figure()
    plt.plot(x,y)
    plt.title('Factor de friccion de Colebrook')
    plt.scatter(raiz,f(raiz))
    plt.text(raiz,f(raiz),' Raiz '+str(raiz),color='red')
    plt.grid()
    
    plt.show()
    fig.savefig("newtonraphson.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()