import numpy as np
import scipy as sp

def gaussSeidel(A,b,x,imax=100,tol=1e-8):
    L=np.tril(A)
    U=A-L
    Linv=np.linalg.inv(L)
    cumple = False
    k=0
    while (not cumple and k<imax):
        xk1=np.dot(Linv,b-np.dot(U,x))
        norma=np.linalg.norm(x-xk1)
        print('iteracion:{}->{} norma {}'.format(k,x,norma))
        cumple=norma<tol
        x=xk1.copy()
        k+=1
        
    if k<imax:
        return x
    else:
        raise ValueError ('El sistema no converge')

def main():
    A = np.array([[-512,12,0,0,0],\
                  [500,-512,12,0,0],\
                  [0,500,-512,12,0],\
                  [0,0,500,-512,12],\
                  [0,0,0,-500,512]])
    b = np.array([0,0,0,0,9])
    x = np.array([0,0,0,0,0])
    x=gaussSeidel(A,b,x)
    print('Solucion: ',x)
        
if __name__ == "__main__": main()