import numpy as np
from scipy import integrate

def regla_trapecios(f,a,b,n):
    h=(b-a)/n
    xs=np.linspace(a,b,n+1)
    ys=f(xs)
    r=h*(ys[0]+2*sum(ys[1:n])+ys[n])/2
    return r

def romberg(f,a,b,epsilon,show=True):
    tabla=np.zeros((20,20),dtype=np.float)
    i=0
    sigue=True
    while sigue:
        n=2**i
        tabla[i,0]=regla_trapecios(f,a,b,n)
        for j in range(1,i+1):
            tabla[i,j]=\
            (np.power(4,j)*tabla[i,j-1]-tabla[i-1,j-1])/(np.power(4,j)-1)
        if i>0:
            sigue=abs(tabla[i,i]-tabla[i-1,i-1])>epsilon
        i+=1
        
    salida=tabla[:i,:i]
    if show:
        print(salida)
    return salida[i-1,i-1]


#funcion a integrar
def f(x):
    return np.exp(x**2)


def main():
    a=0 #limite inferior
    b=1 #limite superior
    error=1e-6 #error permitido
    
    #llamada a la funcion romberg
    integral=romberg(f,a,b,error)
    print(integral)
    
    #llamada a la funcion romberg de scipy
    integral=integrate.romberg(f,a,b,show=True)
    print(integral)
    
if __name__ == "__main__": main()