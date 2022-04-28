import numpy as np

def nr(f,df,x0,tol=1e-5):
    k=0
    while np.abs(f(x0))>tol and k<50:
        if df(x0)!=0:
            x0=x0-f(x0)/df(x0)
        else:
            x0=x0+tol
        k=k+1
    return x0,k