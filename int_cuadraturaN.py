import numpy as np
from scipy.integrate import quadrature,fixed_quad


def cuadraturaN(f,a,b,n):
    w=np.array([[1.,1.],
                [0.55555556,0.88888889,0.55555556],
                [0.3478548,0.6521452,0.6521452,0.3478548],
                [0.2369269,0.4786287,0.5688889,0.4786287,\
                 0.2369269],
                [0.1713245,0.3607616,0.4679139,0.4679139,\
                 0.3607616,0.1713245]])
    
    z=np.array([[-0.577350269,0.577350269],
                [-0.774596669,0,0.774596669],
                [-0.861136312,-0.339981044,0.339981044,\
                 0.861136312],
                [-0.906179846,-0.538469310,0,0.538469310,\
                 0.906179846],
                [-0.932469514,-0.661209386,-0.238619186,\
                 0.238619186,0.661209386,0.932469514]])
    
    s=0
    for i in range(n):
        s+=w[n-2][i]*f((b-a)/2*z[n-2][i]+(a+b)/2)
    r=(b-a)/2*s
    return r

#funcion a integrar
def f(x):
    return 2.41+0.057195*x-4.3e-6*x**2

def main():
    a=300+273.15 #limite inferior
    b=600+273.15 #limite superior
    n=3          #numero de puntos
    
    #llamada a la funcion cuadratura
    area=cuadraturaN(f,a,b,n)
    print('integral = ',area)
    
    
    #llamada a la funcion quadrature de scipy
    area=quadrature(f,a,b)
    print('quadrature = ',area)
    
    #llamada a la funcion fixed_quad de scipy (Gauss)
    area=fixed_quad(f,a,b,(),n)
    print('fixed_quad = ',area)
    
if __name__ == "__main__": main()