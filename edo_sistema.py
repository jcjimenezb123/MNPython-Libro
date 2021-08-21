from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#Sistema de ecuaciones diferenciales
def f(C,t):
    k1=55.2
    k2=30.2
    CH, CM, CX = C
    #C[0] concentracion de Hidrogeno
    #C[1] concentracion de Mesitileno
    #C[2] concentracion de Meta-Xileno
    dch = -k1 * CH ** 0.5 * CM - k2 * CH ** 0.5 * CX  # Hidrogeno
    dcm = -k1 * CH ** 0.5 * CM  # Mesitileno
    dcx =  k1 * CH ** 0.5 * CM - k2 * CH ** 0.5 * CX  # Meta - Xileno
    return [dch,dcm,dcx]


def main():
    x0=0                   #valor inicial de tiempo
    #y0=[Hidrogeno Mesitileno Meta-Xylen]
    y0=[0.021,0.0105,0.]   #condiciones iniciales de 
    x1=0.5                 #valor final del tiempo
    tiempo=np.linspace(x0,x1)
    #llamada a la funcion odeint
    sol=odeint(f,y0,tiempo)
    
    #obtiene la concentracion maxima de meta-xileno X
    cbmax=np.max(sol[:,2])
    #obtiene el indice del valor maximo
    idx=np.where(sol[:,2]==cbmax)
    #obtiene el valor del tiempo del indice
    idx=tiempo[idx]
    print('Concentracion maxima {}, tiempo {}'.format(cbmax,idx))
    #Grafica
    fig=plt.figure()
    plt.plot(tiempo,sol[:,0],label='$Hidrogeno (H)$')
    plt.plot(tiempo,sol[:,1],label='$Mesitileno (M)$')
    plt.plot(tiempo,sol[:,2],label='$Meta-Xileno (X)$')
    plt.legend()
    plt.grid()
    plt.show()
    fig.savefig("edo_sistema.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()                       