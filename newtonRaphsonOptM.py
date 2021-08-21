#importar las funciones de la biblioteca math
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import math 
import cmath 

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
    raiz=optimize.newton(f,x0,fprime=df,fprime2=d2f)
    print('f({:e})={:e}'.format(raiz,f(raiz)))
    
    x=np.linspace(1,5,100)
    y=f(x)
    
    fig = plt.figure()
    plt.plot(x,y)
    plt.title('$f=(x-2)(x-2)(x-4)$')
    plt.scatter(raiz,f(raiz))
    plt.text(raiz,f(raiz),' Raiz '+str(raiz),color='red')
    plt.grid()
    
    plt.show()
    fig.savefig("newtonraphsonoptm.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()