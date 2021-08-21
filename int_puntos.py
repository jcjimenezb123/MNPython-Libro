import numpy as np
from scipy.integrate import trapz,simps

def main():
    x=np.array([1,2,5,6,7,9])
    y=np.array([10,4,11,12,15,12])
    
    #llamada a la funcion trapz y simps (el argumento "y" es primero, luego "x")
    t=trapz(y,x)
    s=simps(y,x)
    
    print('trapecios = ',t)
    print('Simpson = ',s)
    
if __name__ == "__main__": main()