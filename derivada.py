import sympy as sp
f,e,D,Re=sp.symbols('f e D Re')
print(sp.diff(1/sp.sqrt(f)+2*sp.log(e/D/3.7+2.51/(Re*sp.sqrt(f))),f))