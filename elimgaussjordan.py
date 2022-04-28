import numpy as np

def gaussJordan(a,b):
    n,_=np.shape(a)
    A=np.c_[a,b]
    for i in range(n):
        for j in range(n):
            # Si el termino ya es cero continua con la siguiente
            if (A[j,i]!=0 and A[i,i]!=0 and i!=j):
                # factor de reduccion
                f=A[j,i]/A[i,i]
                A[j,i+1:n+1]=A[j,i+1:n+1]-f*A[i,i+1:n+1]
    # aplica la sustitucion inversa
    x=np.zeros(n)
    for i in range(n):
        x[i]=A[i,n]/A[i,i]
        
    return x

def main():
    a=np.array([[0.07, 0.18, 0.15, 0.24 ],\
               [0.03, 0.25, 0.10, 0.65 ],\
               [0.55, 0.41, 0.55, 0.09 ],\
               [0.35, 0.16, 0.20, 0.02 ]])
    b=np.array([0.15*100, 0.25*100, 0.4*100, 0.2*100])
    n,c=np.shape(a)
    r=np.linalg.matrix_rank(a)
    ab=np.c_[a,b]
    ra=np.linalg.matrix_rank(ab)
    
    print('rango(A)={} rango(Ab)={} n={}'.format(r,ra,n))
    
    if (r==ra==n):
        print('solución única')
        x=gaussJordan(a,b)
        #x=np.linalg.solve(a, b)
        print(x)
    
    if (r==ra<n):
        print('múltiples soluciones')
    
    if (r<ra):
        print('sin solución')
        
if __name__ == "__main__": main()