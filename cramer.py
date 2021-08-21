import numpy as np
import scipy as sp

def cramer(A,b):
    dA=np.linalg.det(A)
    _,n=np.shape(A)
    if (dA==0):
        raise ValueError ('El sistema no tiene solucion por la regla de Cramer')
    x=np.zeros(n)
    for i in range(n):
        di=np.copy(A)
        di[:,i]=b
        x[i]=np.linalg.det(di)/dA
        
    return x

def main():
    A=np.array([[3,2,-1],[2,-2,4],[-1,1/2,-1]])
    b=np.array([1,-2,0])
    x=cramer(A,b)
    print(x)
        
if __name__ == "__main__": main()