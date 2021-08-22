import numpy as np
import sympy as sp

def main():
    a=sp.Matrix([[1, 0, 0, 0,-3, 0 ],\
               [ 6 , 0, 0, 0, 0,-1 ],\
               [ 0 , 1,-2, 0, 0, 0 ],\
               [ 0 , 2, 0,-1, 0, 0 ],\
               [ 0 , 8,-3,-2,-4,-1 ]])
    b=sp.Matrix([0,0,0,0,0])
    xvars=sp.symbols('x1,x2,x3,x4,x5,x6')
    x=sp.Matrix(xvars)
    sol=sp.solve(a*x-b,xvars)
    print('Solucion:{}'.format(sol))
    
        
if __name__ == "__main__": main()