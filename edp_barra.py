import numpy as np
import matplotlib.pyplot as plt

def main():
    L=10       #Longitud de la barra
    dx=2       #delta x
    dt=0.1     #delta t
    alfa=0.835 #coeficiente de difusividad termica
    lamda=alfa*dt/dx**2 #valor de lamda
    Ti,Td=100,50     #valores de la frontera (izquierda,derecha)
    
    n=200     #vector tiempo
    m=L//dx   #vector dimension
    u=np.zeros((m+1,n)) #matriz de resultados
    u[0,]=Ti       #se asignan los valores de la frontera
    u[m,]=Td
    
    #calcula la temperatura de cada posicion en cada tiempo
    for ti in range(n-1):
        u[1:m,ti+1]=[u[xi,ti]+lamda*(u[xi-1,ti]-2*u[xi,ti]+u[xi+1,ti])\
          for xi in np.arange(1,m)]
        
    np.set_printoptions(precision=2)
    print (u)
    fig = plt.figure()
    plt.plot(np.linspace(0,L,m+1),u[:,::10])
    plt.title('Temperatura de la barra en el tiempo')
    plt.xlabel('Distancia')
    plt.ylabel('Temperatura')
    fig.savefig("edp_barra.pdf", bbox_inches='tight')
        
if __name__ == "__main__": main()