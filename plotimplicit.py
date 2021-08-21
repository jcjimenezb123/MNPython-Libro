import sympy as syp
x, y = syp.symbols('x, y')

#------------------- Solucion unica
Eq0 = syp.Eq(5*x+2*y,12)
Eq1 = syp.Eq(8*x-4*y,7)

x0,xn=-5,5
y0,yn=-5,5
#fig = syp.figure()
p0 = syp.plot_implicit(Eq0, (x, x0, xn), (y, y0, yn),show=False,label='qwe')

p1 = syp.plot_implicit(Eq1, (x, x0, xn), (y, y0, yn),show=False,line_color='r',label='ec1')

p0.extend(p1)
p0.title='Solución única'
p0.show()
#------------------- Multiple solucion
Eq0 = syp.Eq(5*x+2*y,12)
Eq1 = syp.Eq(10*x+4*y,24)

x0,xn=-5,5
y0,yn=-5,5
#fig = syp.figure()
p0 = syp.plot_implicit(Eq0, (x, x0, xn), (y, y0, yn),show=False,label='qwe')

p1 = syp.plot_implicit(Eq1, (x, x0, xn), (y, y0, yn),show=False,line_color='r',label='ec1')

p0.extend(p1)
p0.title='Multiples soluciones'
p0.show()
#------------------- Sin solucion
Eq0 = syp.Eq(5*x+2*y,12)
Eq1 = syp.Eq(10*x+4*y,10)

x0,xn=-5,5
y0,yn=-5,5
#fig = syp.figure()
p0 = syp.plot_implicit(Eq0, (x, x0, xn), (y, y0, yn),show=False,label='qwe')

p1 = syp.plot_implicit(Eq1, (x, x0, xn), (y, y0, yn),show=False,line_color='r',label='ec1')

p0.extend(p1)
p0.title='Sin solución'
p0.show()
