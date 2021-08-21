#!/usr/local/bin/python
#


# Cargamos las librerias, para asegurarnos de que la
# instalacion ha ido bien
import numpy as np
import matplotlib.pyplot as plt


# Primero definimos una funcion. Cambiar al gusto.
def f(z):
    if (z == complex(0.0)):
        return complex(0.0)
    #val = z**6 + z ** 3 - 1
    #val = z ** 3 - 2*z + 2
    val = z ** 3 - 1

    return val


# Devuelve el resultado del metodo de
# newton empezando en x y ek numero de
# iteraciones
def newton(x):
    h = 1.0e-8
    maxiter = 1000

    err = 100.0
    tol = 1.0e-7
    nit = 0
    while (err > tol):
        der = (f(x + h) - f(x - h)) / (2.0 * h)
        if (der == 0.0):
            return x, 0
        newx = x - f(x) / der
        err = abs(x - newx)
        x = newx
        nit = nit + 1
        if (nit == maxiter):
            return x, nit

    return x, nit


npt = 500
tol = 1.0e-5

x1 = -1.5
x2 = 1.5
hx = (x2 - x1) / npt

y1 = -1.5
y2 = 1.5
hy = (y2 - y1) / npt

nraices = 0
raices = np.zeros(1000, dtype=complex)
raices[0] = complex(0., 0.)
color = np.zeros((npt, npt))
xx = np.zeros(npt)
yy = np.zeros(npt)
for i in range(0, npt):
    xx[i] = x1 + i * hx
    for j in range(0, npt):
        yy[j] = y1 + j * hy
        z = complex(xx[i], yy[j])

        z, nit = newton(z)
        encontrado = False
        for k in range(1, nraices + 1):
            if (abs(z - raices[k]) < tol):
                encontrado = True
                nenc = k
                break

        if (encontrado):
            color[j, i] = float(nenc)
        else:
            print
            'anadida raiz: ', z, nit
            nraices = nraices + 1
            print
            nraices
            raices[nraices] = z
            color[i, j] = float(nraices)

#        print xx[i], yy[j], color[i,j]


CS = plt.imshow(color, cmap=plt.cm.prism , extent=(x1, x2, y1, y2))
plt.xlabel("Parte real")
plt.ylabel("Parte imaginaria")
# plt.colorbar()
plt.show()

