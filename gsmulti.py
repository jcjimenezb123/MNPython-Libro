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
    x1,x2=x
    x1=np.sqrt(x2**2/5) 
    x2=0.25*(np.sin(x1)+np.cos(x2))
    return np.array([x1,x2])

def main():
    x=np.array([0.5,0.5])
    x=gsm(g,x)
    print('Solucion: ',x)
        
if __name__ == "__main__": main()