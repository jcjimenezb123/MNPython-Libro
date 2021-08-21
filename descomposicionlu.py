import numpy as np
import scipy as sp

def main():
    d1=20/1000 #diametro interno de la tuberia en m
    d2=25/1000 #diametro interno de la tuberia en m
    di=35/1000 #espesor del aislante en m
    Ts=150+273 #temperatura del vapor en K
    Ta=25+273  #temperatura ambiente en K
    hi=1500    #coeficiente interior de calor convectivo
    ho=5       #coeficiente exterior de calor convectivo
    ks=45      #coeficiente de conductividad de calor de la tuberia
    ki=0.065   #coeficiente de conductividad de calor del aislante
    d3=d2+2*di #diametro incluyendo el aislante
    
    a=np.array([[2*ks/np.log(d2/d1)+hi*d1,\
                 -2*ks/np.log(d2/d1),\
                 0],
                 [ks/np.log(d2/d1),\
                  -ks/np.log(d2/d1)-ki/np.log(d3/d2),\
                  ki/np.log(d3/d2)],
                 [0,\
                  2*ki/np.log(d3/d2),\
                  -2*ki/np.log(d3/d2)-ho*d3]])
    b=np.array([hi*d1*Ts, 0, -ho*d3*Ta])
    n,c=np.shape(a)
    r=np.linalg.matrix_rank(a)
    ab=np.c_[a,b]
    ra=np.linalg.matrix_rank(ab)
    
    print('rango(A)={} rango(Ab)={} n={}'.format(r,ra,c))
    
    if (r==ra==c):
        print('solucion unica')
        lu, piv = sp.linalg.lu_factor(a)
        x = sp.linalg.lu_solve((lu, piv), b)
        print(lu)
        print(x)
    
    if (r==ra<c):
        print('multiples soluciones')
        
    if (r<ra):
        print('sin solucion')
        
if __name__ == "__main__": main()