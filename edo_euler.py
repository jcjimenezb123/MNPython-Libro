import numpy as np
import matplotlib.pyplot as plt

#Metodo de Euler
def euler(f,x0,y0,x1,n):
    h=(x1-x0)/n      #tamano de paso
    xi=np.zeros(n+1) #vector de x variable independiente
    yi=np.zeros(n+1) #vector de y variable dependiente
    xi[0]=x0         #tiempo iniicial
    yi[0]=y0         #concentracion inicial
    
    for i in range(n):
        yi[i+1]=yi[i]+h*f(xi[i],yi[i])
        xi[i+1]=xi[i]+h
    return xi,yi    #Vector de valores calculados

def f(x,y):
    return -2*y

def f2(x):
    return np.exp(-2*x)*1.5

def main():
    x0=0   #valor inicial de tiempo
    y0=1.5 #valor inicial de la concentracion
    x1=0.6 #valor final del tiempo
    n=20    #numero de pasos
    #llamada a la funcion euler
    x,y=euler(f,x0,y0,x1,n)
    print('x = ',x)
    print('y = ',y)
    
    #Grafica
    fig=plt.figure()
    plt.plot(x,y,'.--',label='Euler')
    plt.plot(np.linspace(x0,x1,50),f2(np.linspace(x0,x1,50)),label='Funcion')
    plt.grid()
    plt.legend()
    plt.title('Metodo de Euler con '+str(n)+' pasos')
    plt.xlabel('tiempo')
    plt.ylabel('Concentracion')
    plt.show()
    #fig.savefig("edo_euler5.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()                       
