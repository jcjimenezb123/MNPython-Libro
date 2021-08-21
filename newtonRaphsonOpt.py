#importar las funciones de la biblioteca math
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import math 
import cmath 

# Funcion a evaluar
def f(x):
    e=0.0015
    D=4
    Re=13743
    return 1/np.sqrt(x)+2*np.log10(e/D/3.7+2.51/Re/np.sqrt(x))

def main():
    # valores iniciales
    x0=0.01
    # Llamada al algoritmo
    raiz=optimize.newton(f,x0)
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
    fig.savefig("newtonraphsonopt.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()