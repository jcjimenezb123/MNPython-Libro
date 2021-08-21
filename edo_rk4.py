import numpy as np
import matplotlib.pyplot as plt

#Metodo de Runge-Kutta
def rungekutta4o(f,x0,y0,x1,n):
    h=(x1-x0)/n      #tamano de paso
    xi=np.zeros(n+1) #vector de x variable independiente
    yi=np.zeros(n+1) #vector de y variable dependiente
    xi[0]=x0         #tiempo iniicial
    yi[0]=y0         #concentracion inicial
    
    for i in range(n):
        k1=f(xi[i],yi[i])
        k2=f(xi[i]+h/2,yi[i]+k1*h/2)
        k3=f(xi[i]+h/2,yi[i]+k2*h/2)
        k4=f(xi[i]+h,yi[i]+k3*h)
        yi[i+1]=yi[i]+h*(k1/6+k2/3+k3/3+k4/6)
        xi[i+1]=xi[i]+h
        
    return xi,yi    #Vector de valores calculados

#ecuacion diferencial
def f(x,y):
    g=32.2
    R=12
    r=1/8
    return -(r**2*np.sqrt(2*g))/(2*R*np.sqrt(y)-np.sqrt(y**3))


def main():
    x0=0    #valor inicial de tiempo
    y0=22   #valor inicial de la altura
    x1=1000 #valor final del tiempo
    n=10    #numero de pasos
    #llamada a la funcion rungekutta4o
    x,y=rungekutta4o(f,x0,y0,x1,n)
    print('x = ',x)
    print('y = ',y)
    #Grafica
    fig=plt.figure()
    plt.plot(x,y,'o--',label='Runge-Kutta 4to orden')
    plt.title('Altura del agua')
    plt.xlabel('tiempo')
    plt.ylabel('Altura')
    plt.legend()
    plt.show()
    #fig.savefig("edo_rungekutta.pdf", bbox_inches='tight')
    
if __name__ == "__main__": main()                       