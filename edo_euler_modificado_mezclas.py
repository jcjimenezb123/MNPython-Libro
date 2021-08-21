import numpy as np
import matplotlib.pyplot as plt

#Metodo de Euler
def euler_mod(f,x0,y0,x1,n):
    h=(x1-x0)/n      #tamano de paso
    xi=np.zeros(n+1) #vector de x variable independiente
    yi=np.zeros(n+1) #vector de y variable dependiente
    xi[0]=x0         #tiempo iniicial
    yi[0]=y0         #concentracion inicial
    
    for i in range(n):
        xi[i+1]=xi[i]+h
        yi[i+1]=yi[i]+h*f(xi[i],yi[i])
        yi[i+1]=yi[i]+h*(f(xi[i],yi[i])+f(xi[i+1],yi[i+1]))/2
        
    return xi,yi    #Vector de valores calculados

def f(x,y):
    return 1.6-0.02*y

def main():
    x0=0   #valor inicial de tiempo
    y0=50  #valor inicial de la concentracion
    x1=30  #valor final del tiempo
    n=30   #numero de pasos
    #llamada a la funcion euler
    x,y=euler_mod(f,x0,y0,x1,n)
    print('x = ',x)
    print('y = ',y)
    
    #Grafica
    fig=plt.figure()
    plt.plot(x,y,'o--',label='Euler Modificado')
    plt.grid()
    plt.legend()
    plt.show()
    fig.savefig("edo_euler_mod_mezclas.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()                       