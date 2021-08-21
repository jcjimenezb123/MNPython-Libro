import numpy as np
import sympy as sp

def main():
    a=np.array([[1 , 0 , -2,  0 ],\
               [ 1 , 0 ,  0, -1 ],\
               [ 3 , 4 , -4, -3 ],\
               [ 0 , 2 ,  0, -1 ],\
               [ 0 , 1 , -1,  0 ]])
    b=np.array([0,0,0,0,0])
    n,c=np.shape(a)
    r=np.linalg.matrix_rank(a)
    ab=np.c_[a,b]
    ra=np.linalg.matrix_rank(ab)
    
    print('rango(A)={} rango(Ab)={} n={}'.format(r,ra,c))
    
    if (r==ra==c):
        print('solucion unica')
        x=np.linalg.solve(a, b)
        print(x)
    
    if (r==ra<c):
        print('multiples soluciones')
        x = sp.Matrix(a).rref()
        print(x)
        
    if (r<ra):
        print('sin solucion')
        
if __name__ == "__main__": main()