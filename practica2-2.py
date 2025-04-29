import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb    # atención: exact=True

""""PRÁCTICA 2.2. Calcular el vector derivada en varios puntos."""
"""XIOMARA GERALDINE CÁCERES CHANCAHUANA"""
"""MARTES 29/04/2025"""

def curvaBezier_vectorDerivada(p, u, ax):

    n = p.shape[0] - 1    # índices de los puntos de control 0,1...n donde n=4
    q = n * (p[1:] - p[:-1])  # Puntos del hodógrafo
    ax.plot(p[:,0], p[:,1], p[:,2], color='k', linestyle='dashed')

    u1d = np.linspace(0, 1, 1001)    # discretizar u en el intervalo [0, 1] con escalón 0.001
    pu_Bezier = np.zeros((3, len(u1d)))    # iniciar con ceros

    Bu_basis = []
    for i in range(n+1):
        Bu_basis.append( comb(n, i, exact=True) * u1d**i * (1-u1d)**(n-i) )
        kp, Bu = np.ix_(p[i], Bu_basis[i])    # kp.ndim y Bu.ndim valen 2
        pu_Bezier += kp * Bu    # kp.shape (3, 1) Bu.shape (1, 1001)

    ax.plot(pu_Bezier[0], pu_Bezier[1], pu_Bezier[2], color='b', linestyle='solid')

    pu = np.zeros(3)

    for i in range(n+1):
        pu += p[i, :] * comb(n, i, exact=True) * u**i * (1 - u)**(n-i)

    ax.scatter(pu[0], pu[1], pu[2], color='red', s=15)

    qu = np.zeros(3)

    for i in range(n):
        qu += q[i, :] * comb(n-1, i, exact=True) * u**i * (1 - u)**(n-1-i)

    f = 0.3
    end_pu = pu + f * qu
    ax.scatter(end_pu[0], end_pu[1], end_pu[2], color='red', s=15)

    ax.plot([pu[0], end_pu[0]], [pu[1], end_pu[1]], [pu[2], end_pu[2]], color='green')


def mainProgram(opt):

    # ndarray de 4+1 puntos de control
    pcontrol = np.array([ 
        [2, 1, 0], 
        [2.5, 2.5, 0.5], 
        [0.5, 2, 1], 
        [0, 1, 1.5], 
        [1, 0, 2.5] 
    ])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') 

    if opt == 1:
        u = 1/3
    elif opt == 2:
        u = 2/3

    curvaBezier_vectorDerivada(pcontrol.copy(), u, ax)

    ax.set_xlim(0, 2.5)      
    ax.set_ylim(0, 2.5)
    ax.set_zlim(0, 2.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Curva de Bézier y vectores tangentes para u={:.2f}'.format(u))


    # Mostrar la gráfica de casteljau
    plt.show()


if __name__ == '__main__':
    while True:
        print("¿Para que valor de u quieres visualizar la curva de Bezier con su vector tangente?")
        u = int(input("1. u=1/3\n"
                    "2. u=2/3\n"))
        if u in (1,2):
            mainProgram(u)
            break
        else:
            print('Opción invalida')