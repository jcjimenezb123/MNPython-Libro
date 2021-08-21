import numpy as np
import matplotlib.pyplot as plt

def main():
    L=10       #Longitud de la barra
    dx=2       #delta x
    dt=0.1     #delta t
    alfa=0.835 #coeficiente de difusividad termica
    lamda=alfa*dt/dx**2 #valor de lamda
    T0 = 0           #temperatura inicial de la barra
    Ti,Td=100,50     #valores de la frontera (izquierda,derecha)
    
    n=200     #vector tiempo
    m=L//dx-1   #vector dimension
    u=np.zeros((m+2,n)) #matriz de resultados
    u[0,]=Ti
    u[m+1,]=Td
    u[1:m,0]=T0
    #calcula la temperatura de cada posicion en cada tiempo
    a=np.zeros((m,m)) #matriz del sistema
    b=np.zeros(m)
    
    #matriz de coeficientes es la misma
    a[0,0:2]=np.array([1+2*lamda,-lamda])
    for i in range(m-2):
        a[i+1,i:i+3]=np.array([-lamda,1+2*lamda,-lamda])
    a[i+2,i+1:i+3]=np.array([-lamda,1+2*lamda])
    #print(a)
    
    #ciclo del tiempo
    for j in range(n-1):
        b[0]=u[1,j]+lamda*u[0,j+1]
        #ciclo de la dimension espacial
        for i in range(m-2):
            b[i+1]=u[i+2,j]
            
        b[m-1]=u[m,j]+lamda*u[m+1,j+1]
        #calculo de las temperaturas (solucion del sistema)
        sol=np.linalg.solve(a, b)
        #asigna resultados
        u[1:m+1,j+1]=sol
    
    np.set_printoptions(precision=4)
    print(u)
    
    fig = plt.figure()
    plt.plot(np.linspace(0,L,m+2),u[:,::10])
    plt.title('Temperatura de la barra en el tiempo')
    plt.xlabel('Distancia')
    plt.ylabel('Temperatura')
    fig.savefig("edp_barra2.pdf", bbox_inches='tight')
        
if __name__ == "__main__": main()