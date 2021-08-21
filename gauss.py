import numpy as np

def gauss(a,b):
    n,_=np.shape(a)
    A=np.c_[a,b]
    for i in range(n-1):
        for j in range(i+1,n):
            # Si el termino ya es cero continua con la siguiente
            if (A[j,i]!=0 and A[i,i]!=0):
                # factor de reducción
                f=A[j,i]/A[i,i]
                # multiplica todo el renglón por el factor
                #for k=i+1:n+1
                #    A(j,k)=A(j,k)-f*A(i,k);
                A[j,i+1:n+1]=A[j,i+1:n+1]-f*A[i,i+1:n+1]
    # aplica la sustitución inversa
    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        #x[i]=A[i,n+1]
        #for j in range(i,n-1):
        #    x[i]=x[i]-x[j+1]*A[i,j+1]
        #x[i]=x[i]/A[i,i]
        x[i]=(A[i,n]-np.dot(A[i,i+1:n],x[i+1:n]))/A[i,i]
        
    return x

def main():
    a=np.array([[1,2,-4],[5,11,-21],[3,-2,3]])
    b=np.array([-4,-22,11])
    n,c=np.shape(a)
    r=np.linalg.matrix_rank(a)
    ab=np.c_[a,b]
    ra=np.linalg.matrix_rank(ab)
    
    print('rango(A)={} rango(Ab)={} n={}'.format(r,ra,n))
    
    if (r==ra==n):
        print('solucion unica')
        x=gauss(a,b)
        #x=np.linalg.solve(a, b)
        print(x)
    
    if (r==ra<n):
        print('multiples soluciones')
    
    if (r<ra):
        print('sin solucion')
        
if __name__ == "__main__": main()