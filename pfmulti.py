import matplotlib.pyplot as plt
import numpy as np

def pfm(g,x,imax=100,tol=1e-8):
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
    return np.array([1/3*np.cos(x[1]*x[2])+1/6,\
                     1/9*np.sqrt(x[0]**2+np.sin(x[2])+1.06)-0.1,\
                     -1/20*np.exp(-x[0]*x[1])-(10*np.pi-3)/60])

def main():
    x=np.array([0.1,0.1,-0.1])
    x=pfm(g,x)
    print('Solucion: ',x)
        
if __name__ == "__main__": main()