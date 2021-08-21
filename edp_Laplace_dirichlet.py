import numpy as np
import matplotlib.pyplot as plt

def main():
    a=np.array([[-4, 1, 0, 1, 0, 0, 0, 0, 0],\
               [1, -4, 1, 0, 1, 0, 0, 0, 0],\
               [0, 1, -4, 0, 0, 1, 0, 0, 0],\
               [1, 0, 0, -4, 1, 0, 1, 0, 0],\
               [0, 1, 0, 1, -4, 1, 0, 1, 0],\
               [0, 0, 1, 0, 1, -4, 0, 0, 1],\
               [0, 0, 0, 1, 0, 0, -4, 1, 0],\
               [0, 0, 0, 0, 1, 0, 1, -4, 1],\
               [0, 0, 0, 0, 0, 1, 0, 1, -4]])
    b=np.array([-100,-20,-20,-80,0,0,-260,-180,-180])
    n,c=np.shape(a)
    r=np.linalg.matrix_rank(a)
    ab=np.c_[a,b]
    ra=np.linalg.matrix_rank(ab)
    
    print('rango(A)={} rango(Ab)={} n={}'.format(r,ra,n))
    
    if (r==ra==n):
        print('solucion unica')
        x=np.linalg.solve(a, b)
        z=x.reshape(3,3)
        print(z)
        X,Y=np.meshgrid(np.arange(1,4), np.arange(1,4))
        
        fig, ax = plt.subplots()
        CS = ax.contour(X, Y, z,10)
        ax.clabel(CS, inline=1, fontsize=10)
        fig.colorbar(CS, shrink=0.8, extend='both')
        ax.set_title('Laplace con condiciones Dirichlet')
        fig.savefig("edp_laplace_dirichlet.pdf", bbox_inches='tight')
    
    if (r==ra<n):
        print('multiples soluciones')
    
    if (r<ra):
        print('sin solucion')
        
if __name__ == "__main__": main()