import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad



#funcion a integrar
def f(x):
    return 1/(1+x**2)

def main():
    a=-np.Infinity #limite inferior
    b=np.Infinity #limite superior
    
    #llamada a la funcion quad de scipy
    area=quad(f,a,b)
    print('quad = ',area)
    
    #grafica de f(x)
    fig=plt.figure()
    x = np.linspace(-5,5,100)
    y = f(x)
    plt.plot(x,y)
    plt.fill_between(x,y)
    
    plt.show()
    fig.savefig("int_impropias2.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()                       