import numpy as np

def gaussSeidel(A,b,x,imax=100,tol=1e-8):
    cumple = False
    n=A.shape[0]
    k=0
    
    while (not cumple and k<imax):
        xk1 = np.zeros(n)
        for i in range(n):
            s1 = np.dot(A[i,:i], xk1[:i])
            s2 = np.dot(A[i,i+1:], x[i+1:])
            xk1[i] = (b[i]-s1-s2)/A[i, i]
            
        norma=np.linalg.norm(x-xk1)
        print('iteracion:{}->{} norma {}'.format(k,xk1,norma))
        cumple=norma<tol
        x=xk1
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
                  [0,0,0,-500,512.0]])
    b = np.array([0,0,0,0,9.0])
    x = np.array([0.0,0.0,0.0,0.0,0.0])
    x=gaussSeidel(A,b,x)
    print('Solucion: ',x)
        
if __name__ == "__main__": main()