import math
import numpy as np
import matplotlib.pyplot as plt


import reglaFalsa as rf

def f(x):
    return np.pi*x**2*(30-x)/3-800


def main():
    # valores iniciales
    x0=4
    x1=6
    tol=1e-4
    # Llamada al algoritmo
    raiz=rf.reglafalsa(f,x0,x1,tol)
    print(raiz)
    
    x=np.linspace(x0,x1,100)
    y=f(x)
    
    fig = plt.figure()
    plt.plot(x,y)
    plt.scatter(raiz,f(raiz))
    plt.text(raiz,f(raiz),' Raiz '+str(raiz),color='red')
    plt.grid()
    
    plt.show()
    #fig.savefig("reglafalsa.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()