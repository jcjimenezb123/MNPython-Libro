import numpy as np
import matplotlib.pyplot as plt

def main():
    a=np.array([[ -2.02, 1, 0, 0, 0, 0, 0, 0, 0 ],\
               [1,-2.02, 1, 0, 0, 0, 0, 0, 0 ],\
               [0, 1,-2.02, 1, 0, 0, 0, 0, 0 ],\
               [0, 0, 1,-2.02, 1, 0, 0, 0, 0 ],\
               [0, 0, 0, 1,-2.02, 1, 0, 0, 0 ],\
               [0, 0, 0, 0, 1,-2.02, 1, 0, 0 ],\
               [0, 0, 0, 0, 0, 1,-2.02, 1, 0 ],\
               [0, 0, 0, 0, 0, 0, 1,-2.02, 1 ],\
               [0, 0, 0, 0, 0, 0, 0, 1,-2.02 ]])
    b=np.array([-50.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-0.5,-200.5])
    n,c=np.shape(a)
    r=np.linalg.matrix_rank(a)
    ab=np.c_[a,b]
    ra=np.linalg.matrix_rank(ab)
    
    print('rango(A)={} rango(Ab)={} n={}'.format(r,ra,n))
    
    if (r==ra==n):
        print('solucion unica')
        x=np.linalg.solve(a, b) #Resuelve el sistema
        print(x)
        L=10   #Longitud de la barra
        n=10   #Pasos
        T0=50  #Condicion en la frontera lado izquierdo
        TL=200 #Condicion en la frontera lado derecho
        x_plot=np.linspace(0,L,n+1) #Vetor de longitud de la barra
        y_plot=np.append([T0],x)     #Agregar el lado izquierdo
        y_plot=np.append(y_plot,[TL])#Agregar el lado derecho
        
        fig=plt.figure()
        plt.plot(x_plot, y_plot)
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("Temperatura")
        plt.show()
        fig.savefig("edo_bvp_diffin.pdf", bbox_inches='tight')
    if (r==ra<n):
        print('multiples soluciones')
    
    if (r<ra):
        print('sin solucion')
        
if __name__ == "__main__": main()