import numpy as np

def gsm(g,x,imax=200,tol=1e-8):
    cumple=False
    k=0
    
    while (not cumple and k<imax):
        x0 = x.copy()
        x=g(x0)
        norma=np.linalg.norm(x-x0)
        print('iteracion:{}->{} norma {}'.format(k,x,norma))
        cumple=norma<tol
        k+=1
        
    if k<imax:
        return x
    else:
        raise ValueError ('El sistema no converge')

def g(x):
    xk1=x.copy()
    xk1[0]=np.sqrt(x[1]**2/5)
    xk1[1]=0.25*(np.sin(x[0])+np.cos(x[1]))
    return xk1

def main():
    x=np.array([0.5,0.5])
    x=gsm(g,x)
    print('Solucion: ',x)
        
if __name__ == "__main__": main()