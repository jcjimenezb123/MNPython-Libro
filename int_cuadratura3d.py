import numpy as np
from scipy.integrate import tplquad

#funcion a integrar NOTA: el argumento "y" debe ser el primero, "x" el segundo
def f(x,y,z):
    return x**2*np.exp(-x**2)*np.exp(-0.5*y*z/x)

def main():
    x1,x2=0,2
    y1,y2=lambda x:0,lambda x:1
    z1,z2=lambda x,y:0,lambda x,y:1
    
    #llamada a la funcion dblquad de scipy
    area,_=tplquad(f,    #funcion a integrar
                 x1,x2,  #limites de x
                 y1,y2,  #limites de y
                 z1,z2   #limites de z
                 ) 
                 
    print('quadrature = ',area)
    
if __name__ == "__main__": main()