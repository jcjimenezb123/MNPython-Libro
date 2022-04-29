import numpy as np
import matplotlib.pyplot as plt

def main():
    L = 10
    dx = 2
    dt = 0.1
    alfa = 0.835
    lamda = alfa * dt / dx ** 2
    T0 = 0
    Tx0 = 100
    Tx10 = 50

    n = 40
    m = L // dx - 1
    u = np.zeros((m + 2, n))
    u[0,] = Tx0
    u[m + 1,] = Tx10
    u[1:m, 0] = T0

    b = np.zeros(m)
    #matriz tri diagonal
    # matriz de coeficientes es la misma
    A = np.diag([-lamda] * (m - 1), -1) + np.diag([2 * (lamda + 1)] * m) + np.diag([-lamda] * (m - 1), 1)

    # ciclo del tiempo
    for j in range(1, n):
        for i in range(m):
            b[i] = lamda * u[i, j - 1] + 2 * (lamda + 1) * u[i + 1, j - 1] + lamda * u[i + 2, j - 1]

        b[0] = b[0] + lamda * u[0, j]
        b[-1] = b[-1] + lamda * u[-1, j]

        # solución del sistema
        sol = np.linalg.solve(A, b)

        # asigna los resultados
        u[1:-1, j] = sol

    #muestra los primeros 5 resultados
    print(u[:,:5].round(4))

    fig = plt.figure()
    plt.plot(np.linspace(0,L,m+2),u[:,::5])
    plt.title('Temperatura de la barra en el tiempo')
    plt.xlabel('Distancia')
    plt.ylabel('Temperatura')
    plt.show()
    fig.savefig("edp_barra3.pdf", bbox_inches='tight')

if __name__ == "__main__": main()