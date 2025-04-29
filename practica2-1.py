import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb    # atención: exact=True

""""PRÁCTICA 2.1. Programar el cálculo de la representación de Casteljau y computar el gráfico de la visualización geométrica."""
"""XIOMARA GERALDINE CÁCERES CHANCAHUANA"""
"""MARTES 29/04/2025"""

# ndarray de 4+1 puntos de control
pcontrol = np.array([ 
    [2, 1, 0], 
    [2.5, 2.5, 0.5], 
    [0.5, 2, 1], 
    [0, 1, 1.5], 
    [1, 0, 2.5] 
])

def casteljauRepresentation(p, u, ax):

    n = p.shape[0] - 1    # índices de los puntos de control 0,1...n donde n=4
    ax.plot(p[:,0], p[:,1], p[:,2], color='k', linestyle='dashed')

    u1d = np.linspace(0, 1, 1001)    # discretizar u en el intervalo [0, 1] con escalón 0.001
    pu_Bezier = np.zeros((3, len(u1d)))    # iniciar con ceros

    Bu_basis = []
    for i in range(n+1):
        Bu_basis.append( comb(n, i, exact=True) * u1d**i * (1-u1d)**(n-i) )
        kp, Bu = np.ix_(p[i], Bu_basis[i])    # kp.ndim y Bu.ndim valen 2
        pu_Bezier += kp * Bu    # kp.shape (3, 1) Bu.shape (1, 1001)

    ax.plot(pu_Bezier[0], pu_Bezier[1], pu_Bezier[2], color='b', linestyle='solid')

    for k in range(1, n+1):
        p = (1 - u) * p[0 : n-k+1, :] + u * p[1 : n-k+2, :]
        ax.plot(p[:,0], p[:,1], p[:,2], color='k', linestyle='dashed')

    ax.scatter(p[0, 0], p[0, 1], p[0, 2], color='red', s=15)





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

    casteljauRepresentation(pcontrol.copy(), u, ax)

    ax.set_xlim(0, 2.5)      
    ax.set_ylim(0, 2.5)
    ax.set_zlim(0, 2.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Representación de Casteljau para u={:.2f}'.format(u))


    # Mostrar la gráfica de casteljau
    plt.show()


if __name__ == '__main__':
    while True:
        print("¿Para que valor de u quieres visualizar la representación de Casteljau?")
        u = int(input("1. u=1/3\n"
                    "2. u=2/3\n"))
        if u in (1,2):
            mainProgram(u)
            break
        else:
            print('Opción invalida')