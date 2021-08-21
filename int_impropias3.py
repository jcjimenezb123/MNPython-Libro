import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#funcion a integrar
def f(x):
    return 1/np.sqrt(x)

def main():
    a=0 #limite inferior
    b=1 #limite superior
    
    #llamada a la funcion quad de scipy
    area=quad(f,a,b)
    print('quad = ',area)
    
    #grafica de f(x)
    fig=plt.figure()
    x = np.linspace(0.1,1,100)
    y = f(x)
    plt.plot(x,y)
    plt.fill_between(x,y)
    
    plt.show()
    fig.savefig("int_impropias3.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()                       