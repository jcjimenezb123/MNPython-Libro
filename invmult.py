import numpy as np
import scipy as sp

def main():
    v=np.array([1000,1200,300,600])
    k=np.array([0.2,0.1,0.3,0.5])
    a=np.array([[1000+v[0]*k[0],0,0,0],\
                [1000,-(1100+v[1]*k[1]),100,0],\
                [0,1100,-(1200+v[2]*k[2]),100],
                [0,0,1100,-(1100+v[3]*k[3])]])
    b=np.array([1000,0,0,0])
    n,c=np.shape(a)
    r=np.linalg.matrix_rank(a)
    ab=np.c_[a,b]
    ra=np.linalg.matrix_rank(ab)
    
    print('rango(A)={} rango(Ab)={} n={}'.format(r,ra,c))
    
    if (r==ra==c):
        print('solucion unica')
        A_inv=np.linalg.inv(a)
        x=np.dot(A_inv,b)
        print(A_inv)
        print(x)
    
    if (r==ra<c):
        print('multiples soluciones')
        
    if (r<ra):
        print('sin solucion')
        
if __name__ == "__main__": main()