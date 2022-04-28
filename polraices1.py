from scipy.optimize import newton

#se define el polinomio
p=lambda x:(50-2*x)*(30-2*x)*x-3000
#se obtiene la primera raíz
r1=newton(p,0)
print(r1)

#se reduce el polinomio 
q=lambda x:p(x)/(x-r1)
#se obtiene la segunda raíz
r2=newton(q,0)
print(r2)

#se reduce el polinomio
s=lambda x:q(x)/(x-r2)
#se obtiene la tercera raíz
r3=newton(s,0)
print(r3)