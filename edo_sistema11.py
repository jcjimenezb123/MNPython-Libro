import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(U, y):
    u1, u2 = U
    alfa = 0.01
    Ta = 25
    du1dy = u2
    du2dy = alfa*(u1-Ta)
    return [du1dy, du2dy]

def main():
    L = 10     # Longitud de la barra
    Tx1 = 50   # temperatura en el extremo x1=0
    Tx2 = 200  # temperatura en el extremo x2=L
    dT = 11.609    # Valor supuesto de la derivada <<<<<<<<<<< Nuevo valor
    
    longitud = np.linspace(0, L) #Vector de la longitud de la barra
    # Solucion del sistema
    U = odeint(f, [Tx1, dT], longitud)
    print('Temperatura en el extremo x2=L : {}'.format(U[-1,0]))
    #Grafica
    fig=plt.figure()
    plt.plot(longitud, U[:,0],label='Tercer tiro')
    plt.plot([L],[Tx2], 'ro',label='Valor esperado')
    plt.legend()
    plt.grid()
    plt.title('Solucion Tiro 3')
    plt.xlabel('Longitud')
    plt.ylabel('Temperarura')
    fig.savefig("edo_bvp11.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()            